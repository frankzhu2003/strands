# DevelocitySA & DevelocityMCP

## Overview
This project provides two main components for interacting with the Develocity API:

- **develocitymcp**: An MCP server that exposes Develocity build information as tools, suitable for use by Strands Agents or other MCP clients.
- **develocitySA**: (Assumed to be a Strands Agent or client) that interacts with the MCP server to retrieve build information from Develocity.

---

## 1. develocitymcp

### Purpose
`develocitymcp.py` is a Python MCP server that exposes tools to:
- Retrieve the latest N build IDs from Develocity
- Retrieve build details by build ID

### Setup
1. [A quick set up from Medium](https://medium.com/techbull/using-aws-strands-with-ollama-0cba83009a2b)
2. **Configure environment variables:**
   ```ini
   export DEVELOCITY_URL=https://your_develocity.com
   export DEVELOCITY_API_KEY=your_develocity_api_key
   ```
   Replace `your_develocity, your_develocity_api_key`.


## 2. develocitySA

### Purpose
`develocitySA` is a Strands Agent, using the local LLM, and compatible client that connects to the `develocitymcp` server to:
- Query for the latest build IDs
- Fetch build details by ID

---

## 3. Run
```python
python -u develocitySA.py
```
The Terminal Output
```
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] initializing MCPClient connection
DEBUG | strands.models.ollama | config=<{'model_id': 'qwen3:latest'}> | initializing
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] entering MCPClient context
DEBUG | strands.tools.mcp.mcp_client | [Thread: Thread-1 (_background_task), Session: 00cab674-9416-4801-b859-041f4278aec0] setting up background task event loop
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] background thread started, waiting for ready event
DEBUG | strands.tools.mcp.mcp_client | [Thread: Thread-1 (_background_task), Session: 00cab674-9416-4801-b859-041f4278aec0] starting async background thread for MCP connection
DEBUG | strands.tools.mcp.mcp_client | [Thread: Thread-1 (_background_task), Session: 00cab674-9416-4801-b859-041f4278aec0] transport connection established
DEBUG | strands.tools.mcp.mcp_client | [Thread: Thread-1 (_background_task), Session: 00cab674-9416-4801-b859-041f4278aec0] initializing MCP session
DEBUG | strands.tools.mcp.mcp_client | [Thread: Thread-1 (_background_task), Session: 00cab674-9416-4801-b859-041f4278aec0] session initialized successfully
DEBUG | strands.tools.mcp.mcp_client | [Thread: Thread-1 (_background_task), Session: 00cab674-9416-4801-b859-041f4278aec0] waiting for close signal
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] the client initialization was successful
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] listing MCP tools synchronously
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] received 2 tools from MCP server
DEBUG | strands.tools.mcp.mcp_agent_tool | tool_name=<get_latest_builds> | creating mcp agent tool
DEBUG | strands.tools.mcp.mcp_agent_tool | tool_name=<get_build_detail_by_id> | creating mcp agent tool
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] successfully adapted 2 MCP tools
DEBUG | strands.tools.registry | tool_name=<get_latest_builds>, tool_type=<python>, is_dynamic=<False> | registering tool
DEBUG | strands.tools.registry | tool_name=<get_build_detail_by_id>, tool_type=<python>, is_dynamic=<False> | registering tool
DEBUG | strands.tools.registry | tools_dir=</Users/fzhu/gradle/ai/strands/tools> | tools directory not found
DEBUG | strands.tools.registry | tool_modules=<[]> | discovered
DEBUG | strands.tools.registry | tool_count=<0>, success_count=<0> | finished loading tools
DEBUG | strands.tools.registry | tools_dir=</Users/fzhu/gradle/ai/strands/tools> | tools directory not found
DEBUG | strands.tools.watcher | tool directory watching initialized
DEBUG | strands.tools.registry | getting tool configurations
DEBUG | strands.tools.registry | tool_name=<get_latest_builds> | loaded tool config
DEBUG | strands.tools.registry | tool_name=<get_build_detail_by_id> | loaded tool config
DEBUG | strands.tools.registry | tool_count=<2> | tools configured
DEBUG | strands.tools.registry | getting tool configurations
DEBUG | strands.tools.registry | tool_name=<get_latest_builds> | loaded tool config
DEBUG | strands.tools.registry | tool_name=<get_build_detail_by_id> | loaded tool config
DEBUG | strands.tools.registry | tool_count=<2> | tools configured
DEBUG | strands.event_loop.streaming | model=<<strands.models.ollama.OllamaModel object at 0x110ea4650>> | streaming messages
DEBUG | strands.types.models.model | formatting request
DEBUG | strands.types.models.model | invoking model
DEBUG | strands.types.models.model | got response from model

Tool #1: get_latest_builds
DEBUG | strands.types.models.model | finished streaming response from model
DEBUG | strands.tools.executor | tool_count=<1>, tool_executor=<ThreadPoolExecutorWrapper> | executing tools in parallel
DEBUG | strands.tools.executor | tool_count=<1> | submitted tasks to parallel executor
DEBUG | strands.handlers.tool_handler | tool=<{'toolUseId': 'get_latest_builds', 'name': 'get_latest_builds', 'input': {'count': 4}}> | invoking
DEBUG | strands.tools.mcp.mcp_agent_tool | invoking MCP tool 'get_latest_builds' with tool_use_id=get_latest_builds
DEBUG | strands.tools.mcp.mcp_client | [Thread: ThreadPoolExecutor-0_0, Session: 00cab674-9416-4801-b859-041f4278aec0] calling MCP tool 'get_latest_builds' synchronously with tool_use_id=get_latest_builds
DEBUG | strands.tools.mcp.mcp_client | [Thread: ThreadPoolExecutor-0_0, Session: 00cab674-9416-4801-b859-041f4278aec0] received tool result with 1 content items
DEBUG | strands.tools.mcp.mcp_client | [Thread: ThreadPoolExecutor-0_0, Session: 00cab674-9416-4801-b859-041f4278aec0] mapping MCP text content
DEBUG | strands.tools.mcp.mcp_client | [Thread: ThreadPoolExecutor-0_0, Session: 00cab674-9416-4801-b859-041f4278aec0] tool execution completed with status: success
DEBUG | strands.event_loop.streaming | model=<<strands.models.ollama.OllamaModel object at 0x110ea4650>> | streaming messages
DEBUG | strands.types.models.model | formatting request
DEBUG | strands.types.models.model | invoking model
DEBUG | strands.types.models.model | got response from model

Tool #2: get_build_detail_by_id

Tool #3: get_build_detail_by_id

Tool #4: get_build_detail_by_id

Tool #5: get_build_detail_by_id
DEBUG | strands.types.models.model | finished streaming response from model
DEBUG | strands.handlers.tool_handler | tool=<{'toolUseId': 'get_build_detail_by_id', 'name': 'get_build_detail_by_id', 'input': {'build_id': 'ppd5k2krzxgq2'}}> | invoking
DEBUG | strands.tools.mcp.mcp_agent_tool | invoking MCP tool 'get_build_detail_by_id' with tool_use_id=get_build_detail_by_id
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] calling MCP tool 'get_build_detail_by_id' synchronously with tool_use_id=get_build_detail_by_id
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] received tool result with 1 content items
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] mapping MCP text content
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] tool execution completed with status: success
DEBUG | strands.handlers.tool_handler | tool=<{'toolUseId': 'get_build_detail_by_id', 'name': 'get_build_detail_by_id', 'input': {'build_id': 'helcpttkl53fa'}}> | invoking
DEBUG | strands.tools.mcp.mcp_agent_tool | invoking MCP tool 'get_build_detail_by_id' with tool_use_id=get_build_detail_by_id
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] calling MCP tool 'get_build_detail_by_id' synchronously with tool_use_id=get_build_detail_by_id
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] received tool result with 1 content items
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] mapping MCP text content
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] tool execution completed with status: success
DEBUG | strands.handlers.tool_handler | tool=<{'toolUseId': 'get_build_detail_by_id', 'name': 'get_build_detail_by_id', 'input': {'build_id': 'wgs32bk2k2uky'}}> | invoking
DEBUG | strands.tools.mcp.mcp_agent_tool | invoking MCP tool 'get_build_detail_by_id' with tool_use_id=get_build_detail_by_id
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] calling MCP tool 'get_build_detail_by_id' synchronously with tool_use_id=get_build_detail_by_id
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] received tool result with 1 content items
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] mapping MCP text content
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] tool execution completed with status: success
DEBUG | strands.handlers.tool_handler | tool=<{'toolUseId': 'get_build_detail_by_id', 'name': 'get_build_detail_by_id', 'input': {'build_id': 'jc3jzeaahcii4'}}> | invoking
DEBUG | strands.tools.mcp.mcp_agent_tool | invoking MCP tool 'get_build_detail_by_id' with tool_use_id=get_build_detail_by_id
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] calling MCP tool 'get_build_detail_by_id' synchronously with tool_use_id=get_build_detail_by_id
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] received tool result with 1 content items
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] mapping MCP text content
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] tool execution completed with status: success
DEBUG | strands.event_loop.streaming | model=<<strands.models.ollama.OllamaModel object at 0x110ea4650>> | streaming messages
DEBUG | strands.types.models.model | formatting request
DEBUG | strands.types.models.model | invoking model
DEBUG | strands.types.models.model | got response from model
<think>
Okay, the user asked for the last 4 builds and then each build's details. First, I called get_latest_builds with count 4, which gave me the build IDs. Then, for each of those IDs, I used get_build_detail_by_id to fetch the details. The responses came back with each build's information. Now, I need to present all these details in a clear way. Let me check if there's any specific information the user might need from these details. They might want to know the build times, tools used, or versions. Since all the builds used Gradle 8.14.2 and the same agent version, maybe the user is checking consistency. I'll summarize the details, highlighting the common elements and the timestamps. Also, ensure the answer is easy to read, maybe listing each build with its ID and availableAt time. No errors in the data, so just present it clearly.
</think>

Here are the details for the last 4 builds:

1. **Build ID:** `ppd5k2krzxgq2`  
   - Available At: 2025-04-15 12:43:09 UTC  
   - Tool: Gradle 8.14.2  
   - Agent: 4.0.2  

2. **Build ID:** `helcpttkl53fa`  
   - Available At: 2025-04-15 12:36:42 UTC  
   - Tool: Gradle 8.14.2  
   - Agent: 4.0.2  

3. **Build ID:** `wgs32bk2k2uky`  
   - Available At: 2025-04-15 12:30:13 UTC  
   - Tool: Gradle 8.14.2  
   - Agent: 4.0.2  

4. **Build ID:** `jc3jzeaahcii4`  
   - Available At: 2025-04-15 12:28:51 UTC  
   - Tool: Gradle 8.14.2  
   - Agent: 4.0.2  

All builds used the same Gradle version and agent. Let me know if you need further analysis!DEBUG | strands.types.models.model | finished streaming response from model
DEBUG | strands.agent.conversation_manager.sliding_window_conversation_manager | window_size=<6>, message_count=<40> | skipping context reduction
<think>
Okay, the user asked for the last 4 builds and then each build's details. First, I called get_latest_builds with count 4, which gave me the build IDs. Then, for each of those IDs, I used get_build_detail_by_id to fetch the details. The responses came back with each build's information. Now, I need to present all these details in a clear way. Let me check if there's any specific information the user might need from these details. They might want to know the build times, tools used, or versions. Since all the builds used Gradle 8.14.2 and the same agent version, maybe the user is checking consistency. I'll summarize the details, highlighting the common elements and the timestamps. Also, ensure the answer is easy to read, maybe listing each build with its ID and availableAt time. No errors in the data, so just present it clearly.
</think>

Here are the details for the last 4 builds:

1. **Build ID:** `ppd5k2krzxgq2`  
   - Available At: 2025-04-15 12:43:09 UTC  
   - Tool: Gradle 8.14.2  
   - Agent: 4.0.2  

2. **Build ID:** `helcpttkl53fa`  
   - Available At: 2025-04-15 12:36:42 UTC  
   - Tool: Gradle 8.14.2  
   - Agent: 4.0.2  

3. **Build ID:** `wgs32bk2k2uky`  
   - Available At: 2025-04-15 12:30:13 UTC  
   - Tool: Gradle 8.14.2  
   - Agent: 4.0.2  

4. **Build ID:** `jc3jzeaahcii4`  
   - Available At: 2025-04-15 12:28:51 UTC  
   - Tool: Gradle 8.14.2  
   - Agent: 4.0.2  

All builds used the same Gradle version and agent. Let me know if you need further analysis!

DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] exiting MCPClient context
DEBUG | strands.tools.mcp.mcp_client | [Thread: Thread-1 (_background_task), Session: 00cab674-9416-4801-b859-041f4278aec0] close signal received
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] waiting for background thread to join
DEBUG | strands.tools.mcp.mcp_client | [Thread: MainThread, Session: 00cab674-9416-4801-b859-041f4278aec0] background thread joined, MCPClient context exited
DEBUG | strands.agent.agent | thread pool executor shutdown complete
```

---

## License
See [Develocity API Terms of Service](https://docs.gradle.com/develocity/api-manual/ref/2025.1.html) for usage restrictions. 
