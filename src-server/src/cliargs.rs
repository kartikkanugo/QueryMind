use clap::Parser;

#[derive(Parser, Debug)]
#[command(version, about = "QueryMind Server")]
pub struct Cli {
    /// Path to configuration file
    #[arg(short, long, default_value = "env.toml")]
    pub config_fp: String, // Config File Path
}
