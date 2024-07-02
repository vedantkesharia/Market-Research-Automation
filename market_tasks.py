from crewai import Task
from textwrap import dedent

class MarketTasks():

    def analyze_market_task(self, agent, markets, investment_period):
        return Task(
            description=dedent(f"""
                Analyze the current trends and potential in various markets
                including gold, silver, crypto, and stock market. This task involves
                gathering data on market performance, identifying trends, and
                evaluating risks and opportunities.

                Your final answer must be a detailed report on each market,
                including performance analysis, trend evaluation, and potential
                investment opportunities.

                Markets: {markets}
                Investment Period: {investment_period}
            """),
            expected_output="A detailed report on each market including performance analysis, trend evaluation, and potential investment opportunities.",
            agent=agent
        )

    def investment_advice_task(self, agent, markets, capital, investment_period):
        return Task(
            description=dedent(f"""
                As a financial advisor, provide investment advice for the specified
                markets. This includes suggesting which assets to buy and hold to
                achieve good profits over the investment period. Consider the
                current market trends and potential risks.

                Your final answer must be a comprehensive investment plan with
                detailed advice on asset allocation, expected returns, and risk
                management strategies.

                Markets: {markets}
                Capital: {capital}
                Investment Period: {investment_period}
            """),
            expected_output="A comprehensive investment plan with detailed advice on asset allocation, expected returns, and risk management strategies.",
            agent=agent
        )

    def diversification_plan_task(self, agent, capital, investment_period):
        return Task(
            description=dedent(f"""
                Develop a diversified investment plan to minimize risks and maximize
                returns. This task involves analyzing different asset classes and
                creating a balanced portfolio.

                Your final answer must be a detailed diversification plan including
                asset allocation, risk assessment, and expected returns.

                Capital: {capital}
                Investment Period: {investment_period}
            """),
            expected_output="A detailed diversification plan including asset allocation, risk assessment, and expected returns.",
            agent=agent
        )




# from crewai import Task
# from textwrap import dedent
# from datetime import date


# class TripTasks():

#     def identify_task(self, agent, origin, cities, interests, range):
#         return Task(
#             description=dedent(f"""
#                 Analyze and select the best city for the trip based
#                 on specific criteria such as weather patterns, seasonal
#                 events, and travel costs. This task involves comparing
#                 multiple cities, considering factors like current weather
#                 conditions, upcoming cultural or seasonal events, and
#                 overall travel expenses.

#                 Your final answer must be a detailed report on the chosen
#                 city, and everything you found out about it, including the
#                 actual flight costs, weather forecast, and attractions.

#                 Traveling from: {origin}
#                 City Options: {cities}
#                 Trip Date: {range}
#                 Traveler Interests: {interests}
#             """),
#             expected_output="A detailed report on the chosen city including flight costs, weather forecast, and attractions.",
#             agent=agent
#         )

#     def gather_task(self, agent, origin, interests, range):
#         return Task(
#             description=dedent(f"""
#                 As a local expert on this city, you must compile an
#                 in-depth guide for someone traveling there and wanting
#                 to have THE BEST trip ever! Gather information about key
#                 attractions, local customs, special events, and daily
#                 activity recommendations. Find the best spots to go to,
#                 the kind of place only a local would know.

#                 This guide should provide a thorough overview of what the
#                 city has to offer, including hidden gems, cultural hotspots,
#                 must-visit landmarks, weather forecasts, and high-level costs.

#                 The final answer must be a comprehensive city guide,
#                 rich in cultural insights and practical tips, tailored
#                 to enhance the travel experience.

#                 Trip Date: {range}
#                 Traveling from: {origin}
#                 Traveler Interests: {interests}
#             """),
#             expected_output="A comprehensive city guide including hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level costs.",
#             agent=agent
#         )

#     def plan_task(self, agent, origin, interests, range):
#         return Task(
#             description=dedent(f"""
#                 Expand this guide into a full 7-day travel itinerary
#                 with detailed per-day plans, including weather forecasts,
#                 places to eat, packing suggestions, and a budget breakdown.

#                 You MUST suggest actual places to visit, actual hotels
#                 to stay, and actual restaurants to go to.

#                 This itinerary should cover all aspects of the trip, from
#                 arrival to departure, integrating the city guide information
#                 with practical travel logistics.

#                 Your final answer MUST be a complete expanded travel plan,
#                 formatted as markdown, encompassing a daily schedule,
#                 anticipated weather conditions, recommended clothing and
#                 items to pack, and a detailed budget, ensuring THE BEST
#                 TRIP EVER. Be specific and give reasons why you picked
#                 each place, and what makes them special!

#                 Trip Date: {range}
#                 Traveling from: {origin}
#                 Traveler Interests: {interests}
#             """),
#             expected_output="A full 7-day travel itinerary in markdown format including daily schedule, weather conditions, recommended clothing, items to pack, and a detailed budget.",
#             agent=agent
#         )
