mongoexport --host 10.100.15.30 --db gd --collection GD_WES_NOTE --out note.json
mongoexport --host 10.100.15.30 --db gd --collection GD_WES_RESULT --out result.json
mongoexport --host 10.100.15.30 --db gd --collection GD_WES_VUS --out vus.json
mongoexport --host 10.100.15.30 --db gd --collection GD_WES_CLINIC --out clinic.json
mongoexport --host 10.100.15.30 --db gd --collection GD_WES_NE_APPENDIX --out negative_appendix.20190912.json
mongoexport --host 10.100.15.30 --db gd --collection GD_WES_SUPPLEMENT_REPORT --out supplement_report.20190912.json
