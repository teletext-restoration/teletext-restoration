# Recovered teletext page restoration
This repository contains recovered UK teletext pages which have been manually restored to correct recovery errors.

These files are **raw teletext packet data** for further analysis and processing. If you're looking for a human readable archive of teletext recoveries which can be read online, see the [Teletext Archaeologist Archive](https://archive.teletextarchaeologist.org/).

## File naming
### Raw recoveries
Teletext recoveries are assigned a systematic filename consisting of the channel, date, start and end time, and 32 bit CRC of the file content.

For example the file `ITV(Yorkshire)-1993-01-03-1355-1415-97C60A0D.t42` contains teletext broadcast on the 3rd of January 1993, in the Yorkshire ITV region, between 1355 and 1415 local time (i.e. as displayed in the page header). The file has a CRC32 of `97C60A0D`.

The recovery files themselves are not stored in this repository for space reasons.

They are currently located at `https://temp.zxnet.co.uk/teletext-recoveries/[filename].7z` where `[filename]` is the systematic base name described above.

e.g. `https://temp.zxnet.co.uk/teletext-recoveries/ITV(Yorkshire)-1993-01-03-1355-1415-97C60A0D.7z`.

Please only download the files you have a use for, and don't try to hoover everything up in one go. Contact <archive@zxnet.co.uk> regarding archive mirroring, bulk processing etc.

#### Recovery notes
For each recovery in the repository there is a corresponding recovery notes file, for example `ITV(Yorkshire)-1993-01-03-1355-1415-97C60A0D-notes.txt` which contains information about the recovery such as the person who performed the recovery, the teletext region name, whether the recovery contains properly recovered page checksums, and if the file does not represent a continuous recording (for example where advert breaks have been removed).

These notes are also present in the archive files, primarily to ensure the recovery credit remains attached to the recovered data.

#### Regions
Different ITV regions are currently stored independently, as are recoveries from S4C. Recoveries from different Channel 4 teletext and Ceefax regions are lumped together.

### Restored pages
Some pages are currently stored in directories named by the start and end time of the recording they are recovered from, e.g. `1355-1415`. The pages are named in the form `Pmpp-ssss.t42` where `m` is the magazine number, `pp` is the page number, and `ssss` is the subpage number.

Most pages contain the time of their first and last transmission during the recording as part of the filename in a common `restored` directory instead of separate directories per recording, i.e. `restored/Pmpp-ssss-hhmm-hhmm.t42`.
This is the preferred form for new restorations, and all files will get renamed to this scheme eventually.

Where the restored pages are close, but do not exactly match any of the CRC checksums present in the recovery (most often because the recovery was made using an old version of vhs-teletext which corrupted them), they are suffixed with the string `-maybe`. For example `P348-0001-1350-1411-maybe.t42`

Where no checksum, or an obviously corrupt checksum (e.g. 0x2020 on every page) was broadcast the filename is sufficed with `-nocrc`.

The location/naming of pages containing regional content, and handling of ambiguous timestamps on daylight saving time changes is yet to be decided.

### Project progress
Progress on restoring various teletext sections (Turner the Worm, Digitiser, Mega-zine, etc.) is currently tracked in a google spreadsheet: https://docs.google.com/spreadsheets/d/1miL8jvurmjmlbHn32wEz7TiPTdzTdR5C6M5ZoliU3o4/edit?usp=sharing
