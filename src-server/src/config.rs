use serde::Deserialize;

#[derive(Debug, Deserialize, Clone)]
pub struct AppConfig {
    pub server_port: u16,
}

impl AppConfig {
    pub fn load() -> Self {
        let settings = config::Config::builder()
            .add_source(config::Environment::default())
            .build()
            .unwrap();

        settings
            .try_deserialize()
            .unwrap_or(AppConfig { server_port: 3000 })
    }
}
