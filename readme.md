# Teletext page restoration
This repository contains recovered teletext pages which have been manually restored to correct recovery errors.

## File naming
### Raw recoveries
 Teletext recoveries are assigned a systematic filename consisting of the channel, date, start and end time, and 32 bit crc of the file content. 
For example the file `ITV(Yorkshire)-1993-01-03-1355-1415-97C60A0D.t42` contains teletext broadcast on the 3rd of January 1993, in the Yorkshire ITV region, between 1355 and 1415 local time (i.e. as displayed in the page header). The file has a CRC32 of `97C60A0D`.

The raw recovery files are not stored in this repository for space reasons. (Hosting of raw files TBD)

#### Recovery notes
For each recovery in the repository there is a corresponding recovery notes file, for example `ITV(Yorkshire)-1993-01-03-1355-1415-97C60A0D-notes.txt` which contains information about the recovery such as the person who performed the recovery, the television region, whether the recovery contains correct checksums, and whether the file does not represent a continuous recording (for example where advert breaks have been removed).
 
#### Regions
ITV regions are currently stored independently, as are recoveries from S4C. Recoveries from different Channel 4 teletext regions are lumped together. 

### Restored pages
Restored pages are currently placed in directories named by the start and end time of the recording they are recovered from, e.g. `1355-1415`. The pages are named in the form `Pmpp-ssss.t42` where `m` is the magazine number, `pp` is the page number, and `ssss` is the subpage number.

Some pages contain the time of their first and last transmission during the recording as part of the filename, i.e. `Pmpp-ssss-hhmm-hhmm.t42`. All files may get renamed to this scheme in due course.

Where the restored pages do not exactly match any of the CRC checksums present in the recovery (most often because the recovery was made using an old version of vhs-teletext which corrupted them) they are suffixed with the string `-maybe`. For example `P348-0001-maybe.t42`

Where no chcksum was broadcast the filename is sufficed with `-nocrc`.

The location/naming of pages containing regional content is yet to be decided.