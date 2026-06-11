# Implementation Plan: Randolph Shoe Care Website

This document outlines the strategy for building the initial concept website for Randolph Shoe Care, incorporating the assets from the client (609-865-6653) and verified Google Business Profile data.

## 1. Project Overview
- **Client:** Randolph Shoe Care
- **Owner:** Randolph
- **Address:** 200 Mercer St, Hightstown, NJ 08520
- **Phone:** (609) 426-4362 / (609) 865-6653
- **Goal:** Build a conversion-optimized, fast single-page website "today".
- **Key Assets:** 
  - Over 60 high-resolution `.JPG` images which have been AI-classified into categories (Dress Shoes, Sneakers, Repairs/Restorations, Products, Storefront).
  - BusinessRate Award Link (`businessrate.com/awards/presentation/v2?cc=XPXXEV`).

## 2. Business Details & Hours
- **Mon:** 9:00 AM – 12:30 PM
- **Tue - Thu:** 9:00 AM – 4:30 PM
- **Fri:** 9:00 AM – 6:00 PM
- **Sat:** 10:00 AM – 2:00 PM
- **Sun:** Closed

## 3. Site Architecture & Content Strategy
We will build a fast, responsive Single Page Application (SPA) focusing on high-quality visual proof, clear services, and the BusinessRate award.

### Sections:
1. **Hero Section:** 
   - Headline: Premium Footwear Restoration & Repair in Hightstown, NJ.
   - Primary Call to Action (CTA): "Call to Book" or "Get a Quote".
   - Hero Image: Use `storefront_1.jpg`.
2. **About/Awards:** 
   - Highlight the recent BusinessRate Award and Randolph's 4.7-star reputation for extraordinary craftsmanship and honest advice.
3. **Services Menu:**
   - **General Repairs:** Fixing heels, soles (leather or rubber), and toe boxes.
   - **Restoration:** Cleaning, polishing, and refinishing leather boots and shoes.
   - **Specialized Work:** Repairing high-end designer shoes (e.g., Giuseppe Zanotti) and complex structural repairs.
4. **Portfolio/Gallery:** 
   - A curated, responsive masonry grid utilizing the categorized images:
     - **Before & After / Repairs:** Filtered using `shoe_repair_*.jpg`
     - **Formal & Leather:** Filtered using `dress_shoes_*.jpg`
     - **Athletic & Sneaker:** Filtered using `sneakers_*.jpg`
5. **Contact/Location:**
   - Embedded Google Map of 200 Mercer St.
   - Listed Hours of Operation.
   - Phone contact info.

## 4. Technical Stack
- **Framework:** HTML5, Tailwind CSS (for rapid, modern styling).
- **Hosting:** Deploy using GitHub Pages for quick, reliable static hosting of the concept.
- **Assets:** Images will be optimized and converted to WebP/AVIF format for fast loading, especially given the large number of files.

## 5. Immediate Next Steps
1. **Image Optimization:** Run a script to compress the categorized `.jpg` files into web-friendly formats.
2. **Development:** Scaffold the `index.html` structure using Tailwind CSS and plug in the business hours, services, and categorized gallery.
3. **Review:** Send the initial Vercel/local link to the client for feedback.