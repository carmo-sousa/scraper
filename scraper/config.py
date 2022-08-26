BASE_URL = "https://argosscan.com/graphql"

HEADERS = {
    "content-type": "application/json; charset=utf-8",
    "content-length": "5098",
    "x-powered-by": "Express",
    "access-control-allow-origin": "*",
    "x-ratelimit-limit": "30",
    "x-ratelimit-remaining": "18",
    "x-ratelimit-reset": "10",
    "cf-cache-status": "DYNAMIC",
    "expect-ct": 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"',
    # "report-to": '{"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=zQzmA7%2B1R55q4V%2FZNyTSuXp8NN5qvoJmbphlcQ4YVLr90y%2BZmMiZuryPIflnmMEsmkZqQbzqHIShckkwBXyrT2d73Casu2ZHWH5NXE4PMYCcIcVQGUR%2BzQSvZRIujpfbRVRzol%2BcslKtGV8F"}],"group":"cf-nel","max_age":604800}',
    "nel": '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}',
    "server": "cloudflare",
    "cf-ray": "73fbf41abb532673-GIG",
    "alt-svc": 'h3=":443"; ma=86400, h3-29=":443"; ma=86400',
}

PROJECT_QUERY = {
    "operationName": "project",
    "variables": {"id": "{project_id}"},
    "query": "query project($id: Int!) {\n  project(id: $id) {\n    id\n    name\n    type\n    adult\n    description\n    alternative\n    authors\n    cover\n    createAt\n    updateAt\n    getChapters(order: {number: DESC}) {\n      id\n      number\n      title\n      createAt\n      __typename\n    }\n    getTags(order: {id: ASC}) {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n}\n",
}

CHAPTER_QUERY = {
    "operationName": "getChapter",
    "variables": {"id": "{chapter_id}"},
    "query": 'query getChapter($id: String!) {\n  getChapters(\n    orders: {orders: {or: ASC, field: "Chapter.id"}}\n    filters: {operator: AND, filters: [{op: EQ, field: "Chapter.id", values: [$id]}], childExpressions: {operator: AND, filters: {op: GE, field: "Project.id", relationField: "Chapter.project", values: ["1"]}}}\n  ) {\n    chapters {\n      id\n      images\n      title\n      number\n      project {\n        id\n        name\n        cover\n        description\n        adult\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
}
