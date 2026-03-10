mod cliargs;
mod conf;
mod errors;
mod models;
mod routes;

use crate::{conf::ServerConfig, errors::ServerError};
use axum::Router;

use cliargs::Cli;
use std::path::Path;
use tracing::info;
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};

#[tokio::main]
async fn main() -> Result<(), ServerError> {
    // Parse Command line args
    let cli_args = Cli::parse()?;

    // load config
    let server_config = ServerConfig::load_config(Path::new(&cli_args.config_fp))?;

    // logging
    tracing_subscriber::registry()
        .with(tracing_subscriber::EnvFilter::new(&server_config.log_lvl))
        .with(tracing_subscriber::fmt::layer())
        .init();

    info!("{}", server_config);
    // build router
    let app = Router::new().merge(routes::chat::router());

    let addr = format!("{}:{}", server_config.address, server_config.port);

    info!("Server running on {}", addr);

    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();

    axum::serve(listener, app).await.unwrap();

    Ok(())
}
