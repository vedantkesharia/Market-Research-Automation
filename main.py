from crewai import Crew
from textwrap import dedent
from market_agents import MarketAgents
from market_tasks import MarketTasks
import os
from dotenv import load_dotenv

load_dotenv()

class MarketCrew:

    def __init__(self, markets, investment_period, capital):
        self.markets = markets
        self.investment_period = investment_period
        self.capital = capital

    def run(self):
        agents = MarketAgents()
        tasks = MarketTasks()

        market_analyst_agent = agents.market_analyst_agent()
        financial_advisor_agent = agents.financial_advisor()
        diversification_expert_agent = agents.diversification_expert()

        analyze_market_task = tasks.analyze_market_task(
            market_analyst_agent,
            self.markets,
            self.investment_period,
        )
        investment_advice_task = tasks.investment_advice_task(
            financial_advisor_agent,
            self.markets,
            self.capital,
            self.investment_period
        )
        diversification_plan_task = tasks.diversification_plan_task(
            diversification_expert_agent,
            self.capital,
            self.investment_period
        )

        crew = Crew(
            agents=[
                market_analyst_agent, financial_advisor_agent, diversification_expert_agent
            ],
            tasks=[analyze_market_task, investment_advice_task, diversification_plan_task],
            verbose=True
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to Market Research Analyzer Crew")
    print('------------------------------------------')
    markets = ["Gold", "Silver", "Crypto", "Stock Market"]
    investment_period = "Next 6 months"
    capital = "100,000 USD"

    market_crew = MarketCrew(markets, investment_period, capital)
    result = market_crew.run()

    # Prepare the output in a formatted way
    output = dedent(f"""
    ########################
    ## Here is your Investment Plan
    ########################

    **Investment Plan Summary:**

    {result}

    """)

    # Write output to a markdown file
    with open('investment_plan1.md', 'w') as file:
        file.write(output)

    print("Investment plan saved to 'investment_plan1.md'")





# from crewai import Crew
# from textwrap import dedent
# from market_agents import MarketAgents
# from market_tasks import MarketTasks
# import os 

# from dotenv import load_dotenv
# load_dotenv()

# class MarketCrew:

#     def __init__(self, markets, investment_period, capital):
#         self.markets = markets
#         self.investment_period = investment_period
#         self.capital = capital

#     def run(self):
#         agents = MarketAgents()
#         tasks = MarketTasks()

#         market_analyst_agent = agents.market_analyst_agent()
#         financial_advisor_agent = agents.financial_advisor()
#         diversification_expert_agent = agents.diversification_expert()

#         analyze_market_task = tasks.analyze_market_task(
#             market_analyst_agent,
#             self.markets,
#             self.investment_period,
#         )
#         investment_advice_task = tasks.investment_advice_task(
#             financial_advisor_agent,
#             self.markets,
#             self.capital,
#             self.investment_period
#         )
#         diversification_plan_task = tasks.diversification_plan_task(
#             diversification_expert_agent,
#             self.capital,
#             self.investment_period
#         )

#         crew = Crew(
#             agents=[
#                 market_analyst_agent, financial_advisor_agent, diversification_expert_agent
#             ],
#             tasks=[analyze_market_task, investment_advice_task, diversification_plan_task],
#             verbose=True
#         )

#         result = crew.kickoff()
#         return result


# if __name__ == "__main__":
#     print("## Welcome to Market Research Analyzer Crew")
#     print('------------------------------------------')
#     markets = ["Gold", "Silver", "Crypto", "Stock Market"]
#     investment_period = "Next 6 months"
#     capital = "100,000 USD"

#     market_crew = MarketCrew(markets, investment_period, capital)
#     result = market_crew.run()
#     print("\n\n########################")
#     print("## Here is your Investment Plan")
#     print("########################\n")
#     print(result)







# # import agentops
# from crewai import Crew
# from textwrap import dedent
# from trip_agents import TripAgents
# from trip_tasks import TripTasks
# import os 

# from dotenv import load_dotenv
# load_dotenv()

# # AGENTOPS_API=os.getenv("AGENTOPS_API")


# # agentops.init(AGENTOPS_API, tags=["trip_planner"])


# class TripCrew:

#     def __init__(self, origin, cities, date_range, interests):
#         self.cities = cities
#         self.origin = origin
#         self.interests = interests
#         self.date_range = date_range

#     def run(self):
#         agents = TripAgents()
#         tasks = TripTasks()

#         city_selector_agent = agents.city_selection_agent()
#         local_expert_agent = agents.local_expert()
#         travel_concierge_agent = agents.travel_concierge()

#         identify_task = tasks.identify_task(
#             city_selector_agent,
#             self.origin,
#             self.cities,
#             self.interests,
#             self.date_range
#         )
#         gather_task = tasks.gather_task(
#             local_expert_agent,
#             self.origin,
#             self.interests,
#             self.date_range
#         )
#         plan_task = tasks.plan_task(
#             travel_concierge_agent,
#             self.origin,
#             self.interests,
#             self.date_range
#         )

#         crew = Crew(
#             agents=[
#                 city_selector_agent, local_expert_agent, travel_concierge_agent
#             ],
#             tasks=[identify_task, gather_task, plan_task],
#             verbose=True
#         )

#         result = crew.kickoff()
#         return result


# if __name__ == "__main__":
#     print("## Welcome to Trip Planner Crew")
#     print('-------------------------------')
#     location = "Atlanta, GA"
#     cities = "Zagreb and Split, Croatia"
#     date_range = "August 5th through August 12th 2024"
#     interests = "Beach, Site Seeing, Nightlife, Food, Culture, History"

#     trip_crew = TripCrew(location, cities, date_range, interests)
#     result = trip_crew.run()
#     print("\n\n########################")
#     print("## Here is you Trip Plan")
#     print("########################\n")
#     print(result)

