FROM nautobot/nautobot:2.0

# Install the nautobot-mcp plugin
COPY . /tmp/nautobot-mcp
RUN pip install /tmp/nautobot-mcp

# Copy default configuration
COPY docker/nautobot_config.py /home/nautobot/nautobot_config.py
ENV NAUTOBOT_CONFIG=/home/nautobot/nautobot_config.py

# Expose the MCP server port
EXPOSE 8005

# Start the MCP server
CMD ["nautobot-server", "start_mcp_server"]
