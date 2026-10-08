"""Temperature sensor simulator - Module 17 logging homework (suggested solution)."""

import logging
import random
import time

logger = logging.getLogger(__name__)

RUN_SECONDS = 180  # 3 minutes; use e.g. 10 while testing
INTERVAL_SECONDS = 1


def setup_logging() -> None:
    """Configure console (all levels) and file (WARNING+) output."""
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)

    log_file = logging.FileHandler("sensor.log", encoding="utf-8")  # bonus
    log_file.setLevel(logging.WARNING)
    log_file.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(console)
    logger.addHandler(log_file)


def log_value(value: int) -> None:
    """Log a single reading with a level that depends on its value."""
    logger.debug("Generated value: %d", value)

    if value > 45:
        logger.critical("Critical temperature: %d", value)
    elif value > 35:
        logger.warning("High temperature: %d", value)
    elif value < 0:
        logger.error("Temperature below zero: %d", value)


def run_sensor(duration: float = RUN_SECONDS, interval: float = INTERVAL_SECONDS) -> list[int]:
    """Generate random temperatures for `duration` seconds and log each one."""
    logger.info("Sensor started for %s seconds", duration)
    values: list[int] = []
    end_time = time.monotonic() + duration

    try:
        while time.monotonic() < end_time:
            value = random.randint(-10, 50)
            values.append(value)
            log_value(value)
            time.sleep(interval)
    except KeyboardInterrupt:  # bonus
        logger.exception("Sensor stopped by user")

    if values:
        logger.info("Sensor finished. Count: %d, min: %d, max: %d", len(values), min(values), max(values))
    else:
        logger.info("Sensor finished. No values generated")
    return values


if __name__ == "__main__":
    setup_logging()
    run_sensor()
