from .utils import make_api_request, build_query_string

def register_cards_tools(mcp):
    """
    Register all card-related tools with the MCP server.
    
    Args:
        mcp: The FastMCP server instance
    """
    
    @mcp.tool()
    def get_cards(
        limit: int = None,
        after: str = None,
        before: str = None
    ) -> dict:
        """
        Get a list of available cards from the Clash Royale API.
        
        Args:
            limit: Limit the number of items returned in the response. (optional)
            
            after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property.
                Note that only after or before can be specified for a request, not both. (optional)
            
            before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property.
                Note that only after or before can be specified for a request, not both. (optional)
        
        Returns:
            Card information including stats, types, etc.
        """
        # Validate that only one of after or before is provided
        if after is not None and before is not None:
            raise ValueError("Only one of 'after' or 'before' can be specified, not both.")
            
        endpoint = "cards"
        
        # Create a dictionary with only the non-None parameters
        queries = {k: v for k, v in {
            "limit": limit,
            "after": after,
            "before": before
        }.items() if v is not None}
        
        if queries:
            endpoint += "?" + build_query_string(queries)
        
        return make_api_request(endpoint)