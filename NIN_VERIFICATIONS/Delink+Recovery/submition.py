curl --location '/delink/' \
--header 'Authorization: Bearer lv_Aijalon_8svgnj9ztf5c4do1m' \
--header 'Content-Type: application/json' \
--data '{
    "number": "12345678901",
    "type": "1" // 1 for (Unlink), 2 for (recovery), 3 for (Unlink & recovery)
}'
