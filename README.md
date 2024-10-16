# Github packages version check

[![test action](https://github.com/m0rr1s-p/check_version/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/m0rr1s-p/check_version/actions/workflows/test.yml)

This GitHub Action takes a GraphQL Query response (using this [Action](https://github.com/octokit/graphql-action))  

## Usage

```yaml
- name: 'Check if version exists for package'
  uses: m0rr1s-p/check_version@main
  id:  getVersion
  with:
    version-number: '0.11.3'  #the version you want to check for
    payload: ${{ steps.get_versions.outputs.data }} # the output of the GraphQL query
- name: Just echo the output
  run: echo '${{ steps.getVersion.outputs.result }}'            

```
|Input|Default|Description|
|-----|-------|-----------|
|version-number|none|The version number you want to check for|
|payload|none|The response of the GitHub GraphQL API|

## GraphQL Query
````yaml
      - uses: octokit/graphql-action@v2.3.2
        id: get_versions
        with:
          query: |
            query versionCheck($package:[String]) {
              viewer {
                packages(names:$package, first: 10) {
                  nodes {
                    versions(first:100){
                      nodes {
                        version
                      }
                    }
                  }
                }
              }
            }
          variables: |
            package: com.mineralminds.protocol.microservice-protocols  # the name of the package
        env:
          GITHUB_TOKEN: ${{ secrets.RO_TOKEN }} # the token with at least read permission on the package
````
This query is in the scope of the viewer. Its needs to be altered to work with organizations.
## License

This project is released under the [MIT License](LICENSE).