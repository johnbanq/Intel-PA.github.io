# Progress report - 8/06/2021 - Kavi

## What I've done

- Submitted probationary review documentation
- Got a reply from NHSX - they say that there are no datasets that have what we're interested in (i.e. transcripts of doctor/patient interactions), but they are working on building an NHS natural language corpus. No work has been done on this corpus as of today, just an [empty github landing page](https://github.com/nhsx/NHS-Language-Corpus) for now.
- Wrote a web scraper to download pages related to diseases and their symptoms on NHS website. It should be noted that the site's `robots.txt` file forbids the scraping of these pages, so I'm unsure if we can publish any findings we encounter as a result of using this data. 
- Switched to a different machine to solve VRAM problem, and can run regular batch sizes. Ran audio augmentation experiments to show that there is a significant difference between different augmentation methods
- Finished the 3rd out of 5 Coursera courses in the Deep Learning specialisation.

## What I'll do next

- Investigate why augmenting datasets via pitch/time shift is more effective than frequency/time masking
- Continue with Coursera