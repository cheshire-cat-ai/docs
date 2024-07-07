# White Rabbit

The White Rabbit is the Cat's built-in scheduler. It is built upon the APScheduler. It enables the scheduling of various type of jobs, including one-time, interval-based and cron jobs. It provides also the capability to handle job execution, pausing, resuming and canceling jobs.

Currently, jobs are stored in memory, but future updates will support database storage for persistent job management.

## How to use

The White Rabbit is a singleton component instantiated during Cat's bootstrap processs. You can easily access it through any Cat instance as follows:

```python

cat.white_rabbit

```

## Methods

| Method | Description | Parameters | Returns |
|--------|-------------|-------------|---------|
| `get_job(job_id: str)` | Retrieves a job by its ID. | `job_id: str` - The ID of the job. | `Dict[str, str]` - Job details or `None` if not found. |
| `get_jobs()` | Returns a list of all scheduled jobs. | None | `List[Dict[str, str]]` - A list of job details. |
| `pause_job(job_id: str)` | Pauses a job by its ID. | `job_id: str` - The ID of the job. | `bool` - `True` if successful, `False` otherwise. |
| `resume_job(job_id: str)` | Resumes a paused job by its ID. | `job_id: str` - The ID of the job. | `bool` - `True` if successful, `False` otherwise. |
| `remove_job(job_id: str)` | Removes a job by its ID. | `job_id: str` - The ID of the job. | `bool` - `True` if successful, `False` otherwise. |
| `schedule_job(job, job_id: str = None, days=0, hours=0, minutes=0, seconds=0, milliseconds=0, microseconds=0, **kwargs)` | Schedules a one-time job to run at a specified time. | `job: function` - The function to be executed. `job_id: str` - The ID of the job (optional). Time parameters (`days`, `hours`, `minutes`, `seconds`, `milliseconds`, `microseconds`). `**kwargs` - Additional arguments for the job function. | `str` - The job ID. |
| `schedule_interval_job(job, job_id: str = None, start_date: datetime = None, end_date: datetime = None, days=0, hours=0, minutes=0, seconds=0, **kwargs)` | Schedules a job to run at regular intervals. | `job: function` - The function to be executed. `job_id: str` - The ID of the job (optional). `start_date: datetime` - The start date of the job (optional). `end_date: datetime` - The end date of the job (optional). Interval time parameters (`days`, `hours`, `minutes`, `seconds`). `**kwargs` - Additional arguments for the job function. | `str` - The job ID. |
| `schedule_cron_job(job, job_id: str = None, start_date: datetime = None, end_date: datetime = None, year=None, month=None, day=None, week=None, day_of_week=None, hour=None, minute=None, second=None, **kwargs)` | Schedules a job using cron-like expressions. | `job: function` - The function to be executed. `job_id: str` - The ID of the job (optional). `start_date: datetime` - The start date of the job (optional). `end_date: datetime` - The end date of the job (optional). Cron time parameters (`year`, `month`, `day`, `week`, `day_of_week`, `hour`, `minute`, `second`). `**kwargs` - Additional arguments for the job function. | `str` - The job ID. |
| `schedule_chat_message(content: str, cat, days=0, hours=0, minutes=0, seconds=0, milliseconds=0, microseconds=0)` | Schedules a chat message to be sent after a specified delay. | `content: str` - The message content. `cat` - The instance of `StrayCat` to send the message. Time parameters (`days`, `hours`, `minutes`, `seconds`, `milliseconds`, `microseconds`). | `str` - The job ID. |

## Examples

Here's a collection of examples showcasing how to use the WhiteRabbit to add scheduling capabilities to your AI agents.

### Schedule a one-time job

In this example, we'll create a simple tool that allows the user to set an alarm that rings after a specified time interval.

```python

from cat.mad_hatter.decorators import tool

@tool
def ring_alarm(wait_time, cat):
    """Useful to ring the alarm. Use it whenever the user wants to ring the alarm. Input is the wait time of the alarm in seconds.""" 

    # Mocking alarm API call
    def ring_alarm_api():
        print("Riiing")

    cat.white_rabbit.schedule_job(ring_alarm_api, seconds=int(wait_time))

    return f"Alarm ringing in {wait_time} seconds"


```

### Schedule an interval job

In this example, we'll build a tool that retrieves a random quote from a free scraping website and sends it to the user at regular intervals.

```python
from cat.mad_hatter.decorators import tool
import requests
import re
import random

@tool(return_direct=True)
def schedule_quote_scraper(interval, cat):
    """
    Useful to get a random quote at a scheduled interval. The interval is in seconds
    """

    def scrape_random_quote():
        url = "http://quotes.toscrape.com/"
        response = requests.get(url)
        response.raise_for_status()
        # We would normally use beautifulsoup here, but for this example we'll just use regex
        quotes = re.findall(r'<span class="text" itemprop="text">(.*?)</span>', response.text)
        if quotes:
            random_quote = random.choice(quotes)
            cat.send_ws_message(random_quote, msg_type="chat")
        else:
            cat.send_ws_message("No quotes found", msg_type="chat")

    # Schedule the job to run at the specified interval
    cat.white_rabbit.schedule_interval_job(scrape_random_quote, seconds=int(interval))

    return f"Quote scraping job scheduled to run every {interval} seconds."



```

### Schedule a cron job

The White Rabbit can also be accessed in hooks to complete generic tasks that are not strictly user-related. For example, it can be used to check for updates of plugins every night at 2:00 AM. You can pass extra arguments to your scheduled function using the `**kwargs` parameter. Please be aware that this is just a basic example. Do not use it in production.

```python
from cat.mad_hatter.decorators import hook
import requests
from cat.mad_hatter.registry import get_registry_url, registry_download_plugin

def parse_version(version: str):
    return tuple(map(int, version.split('.')))

def get_plugins_from_registry(query: str):
    response = requests.post(f"{get_registry_url()}/search", json={"query": query})
    return response.json()

def upgrade_plugin(cat, plugin_id):
    plugin = cat.mad_hatter.plugins[plugin_id]
    plugins = get_plugins_from_registry(plugin.manifest["name"])
    for reg_plugin in plugins:
        if reg_plugin["name"] == plugin.manifest["name"]:
            reg_plugin_version = parse_version(reg_plugin["version"])
            if reg_plugin_version > parse_version(plugin.manifest["version"]):
                tmp_path = registry_download_plugin(reg_plugin["url"])
                cat.mad_hatter.install_plugin(tmp_path)

@hook
def after_cat_bootstrap(cat):
    cat.white_rabbit.schedule_cron_job(patch_plugins, job_id="nightly_upgrade_plugins", hour=2, minute=0, cat=cat, plugin_id="your_fancy_plugin")

```

