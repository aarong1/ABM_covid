#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 00:37:27 2021

@author: aarongorman
"""

#%% 
import sciris as sc
import covasim as cv
import datetime as dt
#import optuna

init_date = dt.datetime.today() - dt.timedelta(days=100)
todays_date = dt.datetime.today()+dt.timedelta(days=42)

#%%
pars = sc.objdict(start_day=init_date,
             end_day=todays_date,
             pop_scale=10,
             pop_size =19e4,
             pop_infected=20e3,
             beta=0.0066,
             frac_susceptible=0.5,
             rel_severe_prob=0.6,
             rel_death_prob=0.8
             )

#%%
sim = cv.Sim(pars=pars,
             datafile='data.csv'
             )


#%%
sim.initialize()
msim=cv.MultiSim(sim)

#%%
msim.run(n_runs=6)

#%%
msim.plot()

#%%

msim.mean()
msim.plot(to_plot=['new_infections','new_deaths','new_severe','cum_deaths','cum_severe'])

#%%
# =============================================================================
# # Create default simulation
# pars = sc.objdict(
#     pop_size       = 20_000,
#     start_day      = '2020-02-01',
#     end_day        = '2020-04-11',
#     beta           = 0.015,
#     rel_death_prob = 1.0,
#     interventions  = cv.test_num(daily_tests='data'),
#     verbose        = 0,
# )
# sim = cv.Sim(pars=pars, datafile='example_data.csv')
# =============================================================================

#%%

# Parameters to calibrate -- format is best, low, high
calib_pars = dict(rel_severe_prob=[pars.rel_severe_prob,0.1,1]   
)

# =============================================================================

    #beta           = [pars.beta, 0.003, 0.009]
# rel_death_prob = [pars.rel_death_prob, 0.05,0.5],
#     frac_susceptible=[pars.frac_susceptible,0.2,0.6],
#     pop_infected    =[pars.pop_infected,1e3,10e3]             

# =============================================================================
#%%
#if __name__ == '__main__':

    # Run the calibration
n_trials = 20
n_workers = 4
calib = sim.calibrate(calib_pars=calib_pars, n_trials=n_trials, n_workers=n_workers)

#%%
#pars.beta=calib.best_pars.beta
pars.rel_severe_prob=calib.best_pars.rel_severe_prob
# =============================================================================
# pars.rel_death_prob=calib.best_pars.rel_death_prob
# pars.frac_susceptible=calib.best_pars.frac_susceptible
# pars.pop_infected=calib.best_pars.pop_infected
# =============================================================================
#%%

sim = cv.Sim(pars=pars,
             datafile='data.csv'
             )

#%%
sim.initialize()
msim=cv.MultiSim(sim)
#%%

msim.run(n_runs=3)

#%%
#msim.plot()

#%%

msim.mean()

#%%
#msim.plot()
#%%

msim.plot(to_plot=['new_infections','new_deaths','new_severe','cum_deaths','cum_severe'])
