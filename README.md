# DE

SELECT 
    COUNT(*) FILTER (WHERE trip_distance <= 1) AS "Up to 1 mile",
    COUNT(*) FILTER (WHERE trip_distance > 1 AND trip_distance <= 3) AS "Between 1 and 3 miles",
    COUNT(*) FILTER (WHERE trip_distance > 3 AND trip_distance <= 7) AS "Between 3 and 7 miles",
    COUNT(*) FILTER (WHERE trip_distance > 7 AND trip_distance <= 10) AS "Between 7 and 10 miles",
    COUNT(*) FILTER (WHERE trip_distance > 10) AS "Over 10 miles"
FROM 
    public.yellow_taxi_data
WHERE 
    lpep_pickup_datetime >= '2019-10-01' 
    AND lpep_dropoff_datetime < '2019-11-01';


select lpep_pickup_datetime 
FROM public.yellow_taxi_data
where trip_distance = (select max(trip_distance) FROM 
    public.yellow_taxi_data)

select concat(z."Borough",' ',z."Zone") as l, sum(py.total_amount) as amount
FROM public.yellow_taxi_data py join zones z on py."PULocationID" = z."LocationID"
where date(py.lpep_pickup_datetime) = '2019-10-18' 
group by z."Borough", z."Zone"
having sum(py.total_amount) > 13000
order by amount desc
limit 3;


select zz."Zone"
FROM yellow_taxi_data pyy join zones zz on pyy."DOLocationID" = zz."LocationID"
where tip_amount = (
select max(tip_amount)
FROM yellow_taxi_data py join zones z on py."PULocationID" = z."LocationID"
where z."Zone" = 'East Harlem North' and py.lpep_pickup_datetime <= '2019-10-31' and py.lpep_pickup_datetime >='2019-10-01')
