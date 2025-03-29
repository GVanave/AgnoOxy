
import os
import requests
from agno.agent import Agent
from agno.models.ollama import Ollama


# Define custom Oxylabs tool
class FuelStationSearchTool:
    def __init__(self):
        self.name = "FuelStationSearchTool"
        self.description = "Fetches nearby fuel stations using Oxylabs Real-Time API."

    def run(self, location_query, pages=1):
        payload = {
            'source': 'google_maps',
            'domain': 'com',
            'query': f'fuel stations in {location_query}',
            'pages': pages,
        }

        

        response = requests.post(
            'https://realtime.oxylabs.io/v1/queries',
            auth=("websearch", "IloveKsop1way+"),
            json=payload,
        )

        if response.status_code != 200:
            return f"API Error: {response.status_code}, {response.text}"

        data = response.json()

        stations_info = []
        for result in data.get('results', [])[:5]:
            title = result.get('title', 'No Name')
            address = result.get('address', 'Address Unavailable')
            rating = result.get('rating', 'Rating Unavailable')
            stations_info.append(f"{title} - {address} (Rating: {rating})")

        if not stations_info:
            return "No nearby fuel stations found."

        return "\n".join(stations_info)

class HotelsSearchTools:
    def __init__(self):
        self.tool_name = "HotelsSearchTool"
        self.description = "Fetches nearby hotels using Oxylabs Real-Time API."

    def run(self, input_location, start_page_no=1):
        input_information = {
        "source": "google_travel_hotels",
            "domain": "com",
            "start_page": start_page_no,
            "query":f"hotels in {input_location}",
        }


        response = requests.post(
            'https://realtime.oxylabs.io/v1/queries',
            auth=("web", "I+"),  #change this
            json=input_information,
        )

        if response.status_code != 200:
            return f"API Error: {response.status_code}, {response.text}"

        data = response.json()

        stations_info = []
        for result in data.get('results', [])[:5]:
            title = result.get('title', 'No Name')
            address = result.get('address', 'Address Unavailable')
            rating = result.get('rating', 'Rating Unavailable')
            stations_info.append(f"{title} - {address} (Rating: {rating})")

        if not stations_info:
            return "No Nearby Hotel found"

        return "\n".join(stations_info)

def hotelsearchagent():
    agent_hotel_search = Agent(
        model=Ollama(id="llama3.2:1b"),
        show_tool_calls=True,
        description="An intelligent logistics assistant helping drivers find nearby services.",
        instructions=[
        "Use HotelsSearchTools to find hotels within a 5 km radius of the user's provided location.",
        "Strictly respond with a structured numbered list following exactly this format:",
        " **Hotel Name:** [Name]",
        "   - **Address:** [Complete Address]",
        "   - **Rating:** [Rating]/5",
        
    ],
        markdown=True,
        tools=[HotelsSearchTools],
    )
    return agent_hotel_search

def fuelstationsearchagent():
    agent = Agent(
    model=Ollama(id="llama3.2:1b"),
    description="An intelligent logistics assistant helping drivers find nearby services.",
    instructions=[
        "Use FuelStationSearchTool for queries about nearby fuel stations.",
        "List fuel stations clearly with names, addresses, and ratings."
    ],
    markdown=True,
    tools=[FuelStationSearchTool()]
    )

    return agent

# Main execution
# if __name__ == "__main__":
#     location_query = "Baramati bus Stand ON"
#     agent.print_response(location_query)