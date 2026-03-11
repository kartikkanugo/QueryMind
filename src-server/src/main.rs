mod cliargs;
mod conf;
mod errors;
mod models;
mod routes;
mod server;

use crate::{conf::ServerConfig, errors::ServerError, server::serve_query_mind};

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
    serve_query_mind(&server_config.address, &server_config.port).await?;

    Ok(())
}
