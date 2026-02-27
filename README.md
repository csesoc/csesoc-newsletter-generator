# CSESoc Newsletter Generator

The web version of the generator is manual. This ensures stability in case Facebook changes the design of their website or if the media article site changes. THe automated version didn't save that much time anyways, and it also required constant changes and maintenance.

We don't actually need a backend for this. But the original newsletter generator code was written in python, so it was decided that the easiest way to conjure up a scrappy version of a manual generator was by having the python code in the backend, which does not require us to edit much code. Note that this is probably not good engineering practice though.

You can deploy both the frontend and backend for free on vercel, or likely on almost any other provider as well.
