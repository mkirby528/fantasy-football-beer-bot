from dotenv import load_dotenv
load_dotenv()
from src.bot import send_message


send_message({
    "event_type": "zero_check"
},{})



# send_message({
#     "event_type": "video_check"
# },{})