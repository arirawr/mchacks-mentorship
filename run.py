#!/usr/bin/env python

from app import app

if __name__ == "__main__":
    app.run(debug=True, port=6543, host="0.0.0.0")
