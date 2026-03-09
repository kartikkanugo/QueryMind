use crate::models::chat::{ChatRequest, ChatResponse};
use axum::{Json, Router, routing::post};

pub fn router() -> Router {
    Router::new().route("/chat", post(chat_handler))
}

async fn chat_handler(Json(payload): Json<ChatRequest>) -> Json<ChatResponse> {
    // placeholder logic
    let reply = format!("You said: {}", payload.message);

    Json(ChatResponse { reply })
}
