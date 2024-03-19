## 📊 Quick Look: Build Duration Trend

### 📚 Session Assumptions

_Prompt:_

#### Rules For Session:

1. When returning code blocks, only return the code that changed and context lines.
2. Add a main function for new scripts if it doesn't exist.
3. Use dotenv for variables like organization, project and personal access token.
4. Only query ADO API for completed builds.
5. Use version 7.1 of the ADO API.
6. Use the ADO REST API for filtering and sorting instead of doing it in code.
7. Use propertyFilters to reduce the amount of data returned.
8. requests.get() should appear as requests.get(url, params=params, auth=(personal_access_token, ''))
9. requests.get() should always use a dict for query params.
10. Use dateutil.parser to parse the date strings.

Let me know if you understand these and when you are ready to continue with the problem.

### 🔍 Query Azure DevOps API

- Iterate on the initial implementation
- Show error recovery

_Prompt:_

```text
I would like a new function to check the build durations for a specific pipeline using the start and finish times. Please create me something to retrieve the last 30 builds.
```

- Show code suggest for main

### 📈 Plot the results Visually

- Build on the MVP

_Prompt:_

```text
Can you create a new function to show me this in an ascii table where the build finish time is the first column and the duration in minutes is the second column with headers.
```

```text
This is great, in addition to showing the build durations in a table, I would like a new function to plot them visually.
```

### 📉 Show the trend

- Gather more insights

_Prompt:_

```text
Great, now can you create a new function to apply a trend line and a legend please?
```

### 🚀 Troubleshooting

- Test the solution

_Prompt:_

```text
It seems like it's returning more than 30 results, can you write me a unit test for get duration to verify?
```

```text
Is it "top" or "$top"?
```