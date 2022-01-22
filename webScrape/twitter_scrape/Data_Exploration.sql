select *from covid.`covid-death`
order by 3,4

select date, continent,location,total_cases,new_cases,total_deaths,population 
From covid.`covid-death`
order by 3,4 

-- #region per continent...
select distinct(continent) as Continents ,
sum(total_deaths) as death_per_continents
from covid.`covid-death`
Group by Continents

-- #ratio death to cases 
select location,date, total_cases, total_deaths, (total_deaths/total_cases) * 100 as Death_per_Case
from covid. `covid-death`

select location,date, total_cases, total_deaths, (total_deaths/total_cases) * 100 as Death_per_Case
from covid. `covid-death`
where location like '%Democratic Republic of Congo%'
order by 3,4

-- #ratio population to cases 
select location,date, total_cases, population, (total_cases/population) * 100 as population_case
from covid. `covid-death`
order by 3,4

-- #Highest infection per population 

select location, population, Max(total_cases) as HighestInfectionCount,
max(total_cases/population) *100 as percentagePopulationInfected 
From covid.`covid-death`
group by location, population
order by percentagePopulationInfected desc


select location,  Max(cast(total_deaths as UNSIGNED INTEGER)) as Total_Deaths
From covid.`covid-death`
Where continent is not null 
group by location
order by Total_Deaths desc

