# from app.usecases.chat import chat, fetch_conversation, propose_conversation_title
import os
from fastapi import APIRouter, Request

from route_schema import (
    BotInput,
    BotMetaOutput,
    BotModifyInput,
    BotOutput,
    BotPinnedInput,
    BotPresignedUrlOutput,
    BotSummaryOutput,
    BotSwitchVisibilityInput,
    ChatInput,
    ChatOutput,
    Content,
    Conversation,
    ConversationMetaOutput,
    Knowledge,
    MessageOutput,
    NewTitleInput,
    ProposedTitle,
    User,
)

from usecases.chat import chat

router = APIRouter()




@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.post("/conversation", response_model=ChatOutput)
def post_message(request: Request, chat_input: ChatInput):
    """Send chat message"""
    # return {"message": chat_input}
    current_user: User = 1

    chat_input = {
        "conversation_id": "1",
        "message": {
            "role": "system",
            "content": {
                    "content_type": "text",
                    "body": "hey",
                    },
            "model": "claude-v2:1",
            "parent_message_id":None
    },
        "bot_id":"5"
        }
    
    output = chat(user_id=current_user.id, chat_input=chat_input)
    print(output,"output")
    return output
