use crate::errors::ServerError;

use crate::routes;
use axum::Router;
use tracing::info;

pub async fn serve_query_mind(address: &str, port: &u16) -> Result<(), ServerError> {
    // build router
    let app = Router::new().merge(routes::chat::router());

    let addr = format!("{}:{}", address, port);

    info!("Server will run on {}", addr);
    let listener = tokio::net::TcpListener::bind(&addr).await?;

    axum::serve(listener, app).await?;

    Ok(())
}
