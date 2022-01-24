---  Alex the Data Analyst 
---- https://www.youtube.com/watch?v=qfyynHBFOsM&list=PLUaB-1hjhk8H48Pj32z4GZgGWyylqv85f

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


-- Total Death by country 

select location,  Max(total_deaths) as Total_Deaths
From covid.`covid-death`
group by location
order by Total_Deaths desc


--- Continent per death per population 

Select continent, MAX(cast(Total_deaths as UNSIGNED Integer)) as TotalDeathCount
From covid.`covid-death`
Where continent is not null 
Group by continent
order by TotalDeathCount desc

---- Global Numbers

Select SUM(new_cases) as total_cases, SUM((new_deaths)) as total_deaths, SUM((new_deaths))/SUM(New_Cases)*100 as DeathPercentage
From covid.`covid-death`
where continent is not null 
Group By date
order by 1,2

--- Total population vs Vaccinations

Select death.continent, death.location,death.date,death.population, vaccin.new_vaccinations
   From covid.`covid-death` death
   join covid.`covid-vaccination`vaccin
   on death.location = vaccin.location
   and death.date    = vaccin.date
where death.continent is not null
order by 1,2,3



Select death.continent, death.location,death.date,death.population, vaccin.new_vaccinations,
   Sum((vaccin.new_vaccinations)) over (Partition by death.location order by death.location,death.date) as RollingPeopleVaccinated
   From covid.`covid-death` death
   join covid.`covid-vaccination`vaccin
   on death.location = vaccin.location
   and death.date    = vaccin.date
where death.continent is not null
order by 2,3



---the number of column in a CTE need to be the same
--- CTE ... Get the ratio (vaccinatedPeople/Population)
with PopsVac(Continent,Location,Date,Population,new_vaccinations,RollingPeopleVaccinated)
as (
Select death.continent, death.location,death.date,death.population, vaccin.new_vaccinations,
   Sum((vaccin.new_vaccinations)) over (Partition by death.location order by death.location,death.date) as RollingPeopleVaccinated
   From covid.`covid-death` death
   join covid.`covid-vaccination`vaccin
   on death.location = vaccin.location
   and death.date    = vaccin.date
where death.continent is not null
order by 2,3
)
select*, (RollingPeopleVaccinated/Population*100) as PercentageVaccination
From PopsVac



-- Using Temp Table to perform Calculation on Partition By in previous query
DROP Table if exists PercentPopulationVaccinated;
Create Table PercentPopulationVaccinated
(
  Continent nvarchar(255),
  Location nvarchar(255),
  Date text,
  Population numeric,
  New_vaccinations text,
  RollingPeopleVaccinated numeric
);
Insert into PercentPopulationVaccinated
(Select death.continent, death.location,death.date,death.population, vaccin.new_vaccinations,
   Sum((vaccin.new_vaccinations)) over (Partition by death.location order by death.location,death.date) as RollingPeopleVaccinated
   From covid.`covid-death` death
   join covid.`covid-vaccination`vaccin
   on death.location = vaccin.location
   and death.date    = vaccin.date
where death.continent is not null
order by 2,3
);
select*, (RollingPeopleVaccinated/Population*100) as PercentageVaccination
From PercentPopulationVaccinated


-- Creating View to store data for later visualizations

Create View PercentPopulationVaccinatedView as
Select death.continent, death.location, death.date, death.population, vaccin.new_vaccinations
, SUM((vaccin.new_vaccinations)) OVER (Partition by death.Location Order by death.location, death.Date) as RollingPeopleVaccinated
-- --, (RollingPeopleVaccinated/population)*100
From covid.`covid-death` death
   join covid.`covid-vaccination`vaccin
  On death.location = vaccin.location
  and death.date = vaccin.date
where death.continent is not null 


