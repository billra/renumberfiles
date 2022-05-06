Work around a bug in gopro image file writing where round 10k numbers are skipped.
(However, every time interval is written, so no information is lost)

E.g.: `"Could not open file : photos/G0020000.JPG"`

This code renumbers JPG files to remove skipped numbers.
