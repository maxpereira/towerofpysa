#!/bin/sh
echo "Grabbing PISA page contents..."
/usr/bin/curl 'https://pisa.ucsc.edu/class_search/index.php' --data 'action=results&binds%5B%3Aterm%5D=2198&binds%5B%3Areg_status%5D=all&binds%5B%3Asubject%5D=&binds%5B%3Acatalog_nbr_op%5D=%3D&binds%5B%3Acatalog_nbr%5D=&binds%5B%3Atitle%5D=&binds%5B%3Ainstr_name_op%5D=%3D&binds%5B%3Ainstructor%5D=&binds%5B%3Age%5D=&binds%5B%3Acrse_units_op%5D=%3D&binds%5B%3Acrse_units_from%5D=&binds%5B%3Acrse_units_to%5D=&binds%5B%3Acrse_units_exact%5D=&binds%5B%3Adays%5D=&binds%5B%3Atimes%5D=&binds%5B%3Aacad_career%5D=&binds%5B%3Asession_code%5D=&rec_start=0&rec_dur=9999' --compressed > /var/www/html/pisa/pisa_raw.txt
now="$(date +'%m/%d/%Y')"
time="$(date +"%T")"
echo "course catalog for fall 2019 last scraped at $time on $now PST (refreshed every half hour)" > /var/www/html/pisa/header.txt
python3.7 /var/www/html/pisa/tower.py
