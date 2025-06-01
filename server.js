require("dotenv").config();
const express = require("express");
const cors = require("cors");
const rateLimit = require("express-rate-limit");
const morgan = require("morgan");
const path = require("path");
const routes = require("./routes");

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.set("trust proxy", true);
app.use(express.json());
app.use(
  rateLimit({
    windowMs: 15 * 60 * 1000,
    max: 100,
    keyGenerator: (req) => {
      return req.ip;
    },
  })
);
app.use(
  morgan(
    ":method :url :status :res[content-length] - :response-time ms :remote-addr"
  )
);

app.use("/plugin", express.static(path.join(__dirname, "plugin")));
// Routes
app.use("/api", routes);

app.use((err, req, res, next) => {
  console.error("Unhandled Error:", err.stack || err);
  res.status(500).json({ error: "Internal Server Error" });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
