use clap::Parser;

use crate::errors::ServerError;

#[derive(Parser, Debug)]
#[command(version, about = "QueryMind Server")]
pub struct Cli {
    /// Path to configuration file
    #[arg(short, long, default_value = "env.toml")]
    pub config_fp: String, // Config File Path
}

impl Cli {
    pub fn parse() -> Result<Self, ServerError> {
        let cli_args = Cli::try_parse()?;
        Ok(cli_args)
    }
}
