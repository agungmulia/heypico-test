"""
title: Google Maps Local Search
author: Agung Mulia
description: A tool Connect Local server Backend to fetch places recomendation from google cloud.
requirements: requests
version: 0.0.1
license: MIT
"""

from typing import Any, Callable
import requests
import json
from pydantic import BaseModel, Field


class EventEmitter:
    def __init__(self, event_emitter: Callable[[dict], Any] = None):
        self.event_emitter = event_emitter

    async def progress_update(self, description):
        await self.emit(description)

    async def error_update(self, description):
        await self.emit(description, "error", True)

    async def success_update(self, description):
        await self.emit(description, "success", True)

    async def emit(self, description="Unknown State", status="in_progress", done=False):
        if self.event_emitter:
            await self.event_emitter(
                {
                    "type": "status",
                    "data": {
                        "status": status,
                        "description": description,
                        "done": done,
                    },
                }
            )


class Tools:
    class Valves(BaseModel):
        CITATION: bool = Field(default="True", description="True or false for citation")
        searchAPI: str = Field(
            default="{{your local hosted network}}/api/v0/maps/places"
        )

    def __init__(self):
        self.valves = self.Valves()
        self.citation = self.valves.CITATION

    async def get_place_suggestions(
        self,
        query: str,
        location: str,
        __event_emitter__: Callable[[dict], Any] = None,
        __user__: dict = {},
    ) -> str:
        """
        Provides place suggestions based on a text query and optional location bias using the Google Maps Text Search (New) API.
        :param query: The text query to search for (e.g., "restaurants in San Francisco").
        :param location_bias: (Optional) A location bias to prioritize results (e.g., circle around a lat/lng).
        :return: Details about the places found or an error message.
        """
        emitter = EventEmitter(__event_emitter__)

        try:
            await emitter.progress_update(f"Searching for places matching: {query}")

            # Determine which API key to use
            searchAPI = self.valves.searchAPI

            # Prepare the API request
            await emitter.progress_update(f"Fetching data for query: {query}")

            headers = {
                "Content-Type": "application/json",
            }

            params = {"query": query, "location": location}

            # Make the API request
            response = requests.get(searchAPI, headers=headers, params=params)

            # Check if the request was successful
            if response.status_code != 200:
                raise Exception(
                    f"API request failed with status code: {response.status_code} - {response.text}"
                )

            # Parse and format the response
            place_json = response.json()

            if not isinstance(place_json, list):
                return "No results found for the given query."

            formatted_places = []
            for i, place in enumerate(place_json, 1):
                name = place.get("name", "Unknown")
                address = place.get("address", "No address")
                map_url = place.get("mapUrl", "No map link")
                formatted_places.append(
                    f"{i}. {name}\n   Address: {address}\n   Maps: {map_url}"
                )
            formatted_output = f"Place suggestions for '{query}':\n\n" + "\n\n".join(
                formatted_places
            )

            # try:
            #     # Try to parse as JSON for better formatting
            #     place_json = json.loads(place_data)
            #     place_data = json.dumps(place_json, indent=2)
            # except:
            #     # If not JSON, use the text as is
            #     pass

            # formatted_output = f"Place suggestions for {query}:\n{place_data}"
            await emitter.success_update(f"Place suggestions for {query} retrieved!")
            return formatted_output

        except Exception as e:
            error_message = f"Error: {str(e)}"
            if "401" in str(e) or "403" in str(e):
                error_message += " (Potential Google Maps API Key issue. Please check your API key and ensure the Places API is enabled.)"
            await emitter.error_update(error_message)
            return error_message
