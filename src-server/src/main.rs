mod config;
mod models;
mod routes;

use axum::Router;
use config::AppConfig;
use tracing::info;
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};

#[tokio::main]
async fn main() {
    // logging
    tracing_subscriber::registry()
        .with(tracing_subscriber::EnvFilter::new("info"))
        .with(tracing_subscriber::fmt::layer())
        .init();

    // load config
    let config = AppConfig::load();

    // build router
    let app = Router::new().merge(routes::chat::router());

    let addr = format!("127.0.0.1:{}", config.server_port);

    info!("Server running on {}", addr);

    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();

    axum::serve(listener, app).await.unwrap();
}
