from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
import openai
from langchain_openai import AzureChatOpenAI

from dotenv import load_dotenv
load_dotenv()

serper = os.getenv('SERPER_API_KEY')

class MarketAgents():
    def __init__(self):
        self.llm = AzureChatOpenAI(
            openai_api_version = "2024-05-01-preview",
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key = os.getenv("AZURE_OPENAI_API_KEY")
        )

    def market_analyst_agent(self):
        return Agent(
            model=os.getenv("MODEL"),
            role='Market Analyst',
            goal='Analyze the current trends in various markets to identify potential investment opportunities',
            backstory='An expert in market analysis with years of experience in identifying profitable trends',
            tools=[
                SearchTools.search_internet,
            ],
            llm=self.llm,
            verbose=True)

    def financial_advisor(self):
        return Agent(
            role='Financial Advisor',
            goal='Provide the best investment advice for maximizing profits over the specified period',
            backstory='A seasoned financial advisor with a deep understanding of different investment markets',
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate,
            ],
            llm=self.llm,
            verbose=True)

    def diversification_expert(self):
        return Agent(
            role='Diversification Expert',
            goal='Create a diversified investment plan to minimize risks and maximize returns',
            backstory='An expert in creating diversified investment portfolios to balance risk and reward',
            tools=[
                SearchTools.search_internet,
            ],
            llm=self.llm,
            verbose=True)









# from crewai import Agent
# from langchain_openai import ChatOpenAI
# import os
# from tools.calculator_tools import CalculatorTools
# from tools.search_tools import SearchTools
# import openai
# from langchain_openai import AzureChatOpenAI

# from dotenv import load_dotenv
# load_dotenv()

# serper = os.getenv('SERPER_API_KEY')
# print(serper)
# # openai.api_type = "azure"
# # openai.api_version = "2024-05-01-preview"
# # openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
# # openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
# # # openai.api_key = os.getenv("OPENAI_API_KEY")
# # print(openai.api_key)
# # endpoint =  os.getenv("AZURE_OPENAI_ENDPOINT")
# # deployment="Gpt4o"
# class TripAgents():
#     def __init__(self):
#         # self.llm = ChatOpenAI(
#         #     model="Gpt4o",
#         #     openai_api_key=os.getenv("OPENAI_API_KEY")
#         #     # azure_endpoint=endpoint,
#         #     # api_version="2024-05-01-preview",
#         #     # model="gpt-4-turbo"
#         # )
#         self.llm = AzureChatOpenAI(
#             openai_api_version = "2024-05-01-preview",
#             azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
#             azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#             api_key = os.getenv("AZURE_OPENAI_API_KEY")
            
#         )

#     def city_selection_agent(self):
#         return Agent(
#             model=os.getenv("MODEL"),
#             role='City Selection Expert',
#             goal='Select the best city based on weather, season, and prices',
#             backstory='An expert in analyzing travel data to pick ideal destinations',
#             tools=[
#                 SearchTools.search_internet,
#             ],
#             llm=self.llm,
#             verbose=True)

#     def local_expert(self):
#         return Agent(
#             role='Local Expert at this city',
#             goal='Provide the BEST insights about the selected city',
#             backstory="""A knowledgeable local guide with extensive information
#         about the city, it's attractions and customs""",
#             tools=[
#                 SearchTools.search_internet,
#             ],
#             llm=self.llm,
#             verbose=True)

#     def travel_concierge(self):
#         return Agent(
#             role='Amazing Travel Concierge',
#             goal="""Create the most amazing travel itineraries with budget and 
#         packing suggestions for the city""",
#             backstory="""Specialist in travel planning and logistics with 
#         decades of experience""",
#             tools=[
#                 SearchTools.search_internet,
#                 CalculatorTools.calculate,
#             ],
#             llm=self.llm,
#             verbose=True)
