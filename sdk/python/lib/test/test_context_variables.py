# Verify that pulumi can create two resources at the same time with multiple threads.

import asyncio
from concurrent.futures import ThreadPoolExecutor