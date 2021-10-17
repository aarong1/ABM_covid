library(readxl)
library(tidyverse)

build_training <- function(date_from='2021-07-06') {
  
  print(as.Date({{date_from}}))
  Tests <- read_excel("doh-dd-141021.xlsx", 
      sheet = "Tests", 
      col_types = c("date", 
          "text", "numeric", "numeric", "numeric"))
  
  Tests <- Tests%>%
    count(`Date of Specimen`,wt=`Individ with Positive Lab Test`,name='new_infections')%>%
    filter(`Date of Specimen`>=as.Date({{date_from}}))%>%
        mutate(cum_infections=cumsum(new_infections)+10^5)%>%
    rename(date=`Date of Specimen`)

  Deaths  <- read_excel("doh-dd-141021.xlsx", 
      sheet = "Deaths", 
      col_types = c("date", 
          "text", "text", "text", "text", "numeric"))
  
  Deaths <- Deaths%>%
    count(`Date of Death`,wt = `Number of Deaths`,name='new_deaths')%>%
    filter(`Date of Death`>=as.Date(date_from))%>%
    rename(date=`Date of Death`)
  
  severe <- read_excel("doh-dd-141021.xlsx", 
    sheet = "Admissions", col_types = c("date", 
        "text", "text", "date", "text", "text", 
        "numeric"))

  severe <- severe%>%
    count(`Admission Date`,wt=`Number of Admissions`,name='new_severe')%>%
      filter(`Admission Date`>=as.Date({{date_from}}))%>%
    rename(date=`Admission Date`)
    
  left_join(Tests,Deaths,by=c('date'))%>%
    left_join(.,severe,by='date')%>%
    replace_na(replace = list(0,new_infections=0,cum_infections=0,new_deaths=0,new_severe=0))%>%
    write.csv('data.csv',row.names = FALSE)
  
}

build_training()
build_training(date='2020-03-01')

Tests%>%
    count(`Date of Specimen`,wt=`Individ with Positive Lab Test`,name='new_infections')%>%
    mutate(cum_infections=cumsum(new_infections)+10^4)

library(readxl)

