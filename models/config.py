# models/config.py
import json
import os
from typing import Any, Optional

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "lin_speed": 30,
    "fix_speed": 30,
    "pre_speed": 30,
    "post_speed": 30,
    "fan_speed": 50,
    "lin_position": 0,
    "pre_position": 0,
    "lin_pos1": 0,
    "lin_pos2": 0,
    "target_pre_force": 0.0,
    "torque_max": 0.0,
    "torque_min": 0.0,
    "force_max": 0.0,
    "force_min": 0.0,
    "current_max": 0.0,
    "current_min": 0.0,
    "temp_min": 40.0,
    "temp_max": 70.0,
    "start_speed": 30,
}


class Config:    
    _instance = None
    _config = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._config = cls._load_config()
        return cls._instance
    
    @staticmethod
    def _load_config() -> dict:
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return DEFAULT_CONFIG.copy()
        return DEFAULT_CONFIG.copy()
    
    def _save(self) -> None:
        try:
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, indent=4, ensure_ascii=False)
        except IOError:
            pass
    
    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        self._config[key] = value
        self._save()
    
    def get_all(self) -> dict:
        """Получение всей конфигурации"""
        return self._config.copy()

def get_config_value(key: str, default: Any = None) -> Any:
    return Config().get(key, default)


def set_config_value(key: str, value: Any) -> None:
    Config().set(key, value)