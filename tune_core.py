#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Oct 14 19:50:42 2021

@author: aarongorman
"""
import covasim as cv
import datetime as dt
#%%


todays_date = dt.datetime.today()
# start todays date 
init_date = dt.datetime.today() - dt.timedelta(days=100)
start_day = str((todays_date-dt.timedelta(days=50)).date())


#%%

sim = cv.Sim(start_day=init_date,
             end_day=todays_date,
             pop_scale=10,
             pop_size =19e4,
             pop_infected=10e3, # if we cahange this we must change the prep file
             beta=0.007,
             frac_susceptible=0.5,
             rel_death_prob=0.3,
             datafile='data.csv'
             )



#%%
sim.initialize()
msim = cv.MultiSim(sim)


#%%

msim.run(n_runs=8,
         )


#%%

msim.plot()

#%%
msim.plot(to_plot=['new_infections','new_severe','new_deaths'])


#%%
msim.mean()

#%%
msim.plot(to_plot=['new_infections','cum_infections','new_deaths','cum_deaths'])

#%%
#demo interventions

def open_schools(sim):
    if sim.t == sim.day('2021-09-01'):
        young_people = sim.people.age<18
        sim.people.rel_sus[young_people] = 2.0
        
        
#%%
pars = dict(start_day=init_date,
             end_day=todays_date,
             pop_scale=100,
             pop_size =19e3,
             pop_infected=10e3,
             beta=0.007,
             frac_susceptible=0.5,
             rel_death_prob=0.5)


#%%
sim=cv.Sim(pars,n_days=200,interventions=open_schools, label='open_schools-double_child_susceptibility')
sim2=cv.Sim(pars,n_days=200)
msim=cv.MultiSim([sim,sim2])
msim.run(n_runs=10)
msim.plot()
