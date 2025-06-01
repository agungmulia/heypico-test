class GoogleMapsService {
  constructor(apiKey = "", httpClient) {
    this.apiKey = apiKey;
    this.httpClient = httpClient;
  }


  async searchPlaces(query, location) {
    const url = `https://maps.googleapis.com/maps/api/place/textsearch/json`;
    const response = await this.httpClient.get(url, {
      params: {
        query: query,
        location: location,
        radius: 5000,
        key: this.apiKey,
      },
    });

    console.log("masuk kesini bang");


    return response.data.results.map((place) => ({
      name: place.name,
      address: place.formatted_address,
      locationUrl: `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(
        place.name
      )}`,
    }));
  }
}

exports.GoogleMapsService = GoogleMapsService;
