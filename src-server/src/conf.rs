use crate::errors::ServerError;
use config::{Config, File, FileFormat, FileSourceFile};
use serde::Deserialize;
use std::fmt;
use std::path::Path;

#[derive(Debug, Deserialize)]
pub struct ServerConfig {
    pub address: String,
    pub port: u16,
    pub log_lvl: String,
}

impl ServerConfig {
    pub fn load_config(fp: &Path) -> Result<Self, ServerError> {
        let toml_data = Config::builder().add_source(File::from(fp)).build()?;
        let server_conf = toml_data.get::<ServerConfig>("server")?;
        Ok(server_conf)
    }
}

impl fmt::Display for ServerConfig {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "ServerConfig {{address: {}, port: {}, log_lvl: {}}}",
            self.address, self.port, self.log_lvl
        )
    }
}
