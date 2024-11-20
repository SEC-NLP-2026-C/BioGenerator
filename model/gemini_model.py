import os
import json 
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from dotenv import load_dotenv



        

class GeminiModel:
    def __init__(self):
        
        load_dotenv("model\\secrets.env")

        # Configure Gemini API
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        
        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 60,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            properties = {
            "response": content.Schema(
                type = content.Type.STRING,
            ),
            },
        ),
        "response_mime_type": "application/json",
        }

        # Call the Gemini API
        self.model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        )

    def generate_response(self, career, personality, interests, relationship_goals):
         
        response = self.model.generate_content([
        "User Input Career: Chef\nPersonality: Creative\nInterests: Culinary Arts, Traveling\nRelationship Goals: Long-term",
        "Output The Culinary Explorer\n\nAdventurous chef with a flair for international cuisine and a love for travel. Searching for a partner to explore exotic flavors and cultures together.",
        "User Input Career: Teacher\nPersonality: Compassionate\nInterests: Literature, Mentoring\nRelationship Goals: Seeking Deep Connection",
        "Output The Thoughtful Mentor\n\nDedicated teacher with a passion for nurturing young minds and exploring classic literature. Hoping to find someone who values kindness and intellectual depth.",
        "User Input Career: Artist\nPersonality: Adventurous\nInterests: Nature, Sculpting\nRelationship Goals: Adventurous",
        "Output The Wanderlust Artist\n\nFree-spirited artist inspired by the beauty of nature and a love for sculpting. Seeking an adventurous soul to wander the world and create masterpieces with.",
        "User Input Career: Entrepreneur\nPersonality: Creative\nInterests: Technology, Startups\nRelationship Goals: Long-term",
        "Output The Visionary Creator\n\nInnovative entrepreneur driven by technology and creative ideas. Looking for a partner who shares my vision and excitement for building the future together.",
        "User Input Career: Musician\nPersonality: Outgoing\nInterests: Live Performances, Festivals\nRelationship Goals: Casual",
        "Output The Festival Enthusiast\n\nVibrant musician with a love for live performances and music festivals. Seeking someone who can keep up with my rhythm and share unforgettable nights under the stars.",
        "User Input Career: Software Engineer\nPersonality: Introverted\nInterests: Coding, Problem-Solving\nRelationship Goals: Seeking Deep Connection",
        "Output The Code Whisperer\n\nQuiet and focused software engineer who finds joy in solving complex puzzles. Searching for a deep connection with someone who appreciates quiet evenings and meaningful conversations.",
        "User Input Career: Chef\nPersonality: Compassionate\nInterests: Baking, Volunteering\nRelationship Goals: Long-term",
        "Output The Sweet-Hearted Baker\n\nCaring chef with a talent for creating sweet treats and a heart for giving back. Hoping to find a partner who values kindness and shares my love for baking.",
        "User Input Career: Teacher\nPersonality: Outgoing\nInterests: Traveling, Cultural Exchange\nRelationship Goals: Adventurous",
        "Output The Cultural Storyteller\n\nEnthusiastic teacher passionate about traveling and cultural exchange. Looking for an adventurous companion to share stories and discover the world together.",
        "User Input Career: Artist\nPersonality: Introverted\nInterests: Painting, Poetry\nRelationship Goals: Seeking Deep Connection",
        "Output The Poetic Painter\n\nReflective artist who blends the beauty of painting with the rhythm of poetry. Seeking a meaningful connection with someone who sees the world through a creative lens.",
        "User Input Career: Entrepreneur\nPersonality: Adventurous\nInterests: Startups, Traveling\nRelationship Goals: Casual",
        "Output The Maverick Adventurer\n\nBold entrepreneur with a passion for startups and exploring uncharted paths. Looking for someone who thrives on spontaneity and exciting adventures.",
        "User Input Career: Musician\nPersonality: Creative\nInterests: Songwriting, Nature\nRelationship Goals: Long-term",
        "Output The Melodic Dreamer\n\nSoulful musician inspired by nature and storytelling through songs. Searching for a long-term partner to create harmonies both on and off stage.",
        "User Input Career: Software Engineer\nPersonality: Outgoing\nInterests: Gaming, Esports\nRelationship Goals: Adventurous",
        "Output The Esports Enthusiast\n\nDynamic software engineer who brings the same energy to coding as to esports. Hoping to find a partner who enjoys gaming adventures and thrilling competitions.",
        "User Input Career: Chef\nPersonality: Adventurous\nInterests: Fusion Cuisine, Hiking\nRelationship Goals: Adventurous",
        "Output The Gourmet Explorer\n\nTrailblazing chef with a love for fusion cuisine and outdoor adventures. Seeking someone to hike, cook, and savor life’s flavors together.",
        "User Input Career: Teacher\nPersonality: Creative\nInterests: Writing, Theater\nRelationship Goals: Long-term",
        "Output The Dramatic Educator\n\nInnovative teacher with a passion for storytelling and theater. Looking for a long-term partner to create a meaningful and inspiring life narrative.",
        "User Input Career: Artist\nPersonality: Compassionate\nInterests: Photography, Wildlife\nRelationship Goals: Seeking Deep Connection",
        "Output The Compassionate Lens\n\nEmpathetic artist who captures the soul of wildlife through photography. Searching for a deep connection with someone who values creativity and nature.",
        "User Input Career: Architect\nPersonality: Adventurous\nInterests: Cooking, Traveling\nRelationship Goals: Adventurous",
        "Output The Adventurous Foodie\n\nGlobe-trotting architect with a passion for spicy food and sustainable design. Seeking a fellow adventurer who can appreciate a good biryani and a thought-provoking conversation.",
        "User Input Career: Writer\nPersonality: Introverted\nInterests: Literature, Coffee\nRelationship Goals: Seeking Deep Connection",
        "Output The Creative Bookworm\n\nIntroverted writer with a love for classic literature and indie coffee shops. Looking for someone who can match my wit and charm over a cup of chai and a deep discussion about our favorite novels.",
        "User Input Career: Entrepreneur\nPersonality: Energetic\nInterests: Fitness, Outdoor Adventures\nRelationship Goals: Long-term",
        "Output The Sporty Entrepreneur\n\nEnergetic entrepreneur with a passion for fitness and outdoor adventures. Seeking a partner who can keep up with my active lifestyle and shares my love for hiking, biking, and trying new things.",
        "User Input Career: Musician\nPersonality: Compassionate\nInterests: Live Music, Social Justice\nRelationship Goals: Casual",
        "Output The Compassionate Musician\n\nSoulful musician with a heart for social justice and a love for live music. Looking for a kind and compassionate partner who enjoys jamming out at concerts and making a difference in the world.",
        "User Input Career: Software Engineer\nPersonality: Tech-Savvy\nInterests: Gaming, Technology\nRelationship Goals: Casual",
        "Output The Tech-Savvy Gamer\n\nSoftware engineer by day, gamer by night. I'm equally comfortable debugging code and exploring virtual worlds. Seeking a partner who can appreciate my geeky side and isn't afraid to challenge me to a board game showdown.",
        "User Input Career: "+str(career) + "\nPersonality: " + str(personality) + "\nInterests: " + str(interests) + "\nRelationship Goals: " + str(relationship_goals),
        "Output ",
        "the output should include both topic and description. it should also be capitilized properly."
        ])


        formatted_response = json.loads(response.text)
        inner_json = json.loads(formatted_response['response'])
        print(response)
        output_topic = inner_json["topic"]
        output_description = inner_json["description"]

        return output_topic, output_description
    

    