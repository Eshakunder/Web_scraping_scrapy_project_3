# Quotes Login Scraper (Scrapy)

A **Scrapy spider** that demonstrates how to **log in to a website and scrape data after authentication**.  
The spider logs into **Quotes to Scrape** and extracts quotes, authors, and tags from the page.

## Features

- Demonstrates **form-based login scraping**
- Extracts **CSRF token** from the login form
- Sends login request using **Scrapy FormRequest**
- Scrapes:
  - Quote text
  - Author name
  - Quote tags
- Uses **Scrapy Items** for structured data
- Uses `open_in_browser()` for debugging login responses

## Target Website

https://quotes.toscrape.com
