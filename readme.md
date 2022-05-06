Work around a bug in gopro image file writing where round 10k numbers are skipped.
(However, every time interval is written, so no information is lost)

E.g.: `"Could not open file : photos/G0020000.JPG"`

This code renumbers JPG files to remove skipped numbers.

example run:

    (ffmpeg) C:\Users\billr\Desktop\moviework>python renumberfiles.py photos
    renumber files
    found 50045 files in photos
    first: G0018748.JPG
    last: G0068797.JPG
    missing 20000, got 20001, offset is now 1
    missing 30000, got 30001, offset is now 2
    missing 40000, got 40001, offset is now 3
    missing 50000, got 50001, offset is now 4
    missing 60000, got 60001, offset is now 5
    end.
