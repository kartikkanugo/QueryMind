use config::ConfigError;
use thiserror::Error;

#[derive(Debug, Error)]
pub enum ServerError {
    #[error("Invalid CLI Args: {0}")]
    InvalidCliArgs(#[from] clap::Error),

    #[error("Configuration error: {0}")]
    Config(#[from] ConfigError),

    #[error("Server IO error: {0}")]
    ServerIO(#[from] std::io::Error),

    #[error("Network error: {0}")]
    Network(String),

    #[error("Internal server error")]
    Internal,
}
