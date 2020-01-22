Solr is available to install as a Docker container. This is the easiest way to get a Solr instance up and running, so let's get started. 

Install and run the latest available Solr container image:

`docker run -d --name=solr solr`{{execute}}

Let's check that the container is now running: 

`docker ps`{{execute}}

You can see the `ID`, `NAME` and `STATUS` of our new container. 

Now, we want to connect to our Solr container and begin running commands:

`docker exec -it solr /bin/bash`{{execute}}

Solr manages your content in separate indexes called _Cores_. Each core manages a separate set of configuration files, logs and data. Let's create a core called `techproducts`. 

`bin/solr create -c techproducts -s 2 -rf 2`{{execute}}

We tell Solr to create two partitions with the `-s` flag and two replicas with the `-rf` command. When building production Solr cores, you will change these values to your individual needs. 

Now, let's load some sample data to our core: 

`bin/post -c techproducts example/exampledocs/*.xml`{{execute}}

This command uses the built-in `post` binary which comes with Solr. We loaded some sample `xml` files which contain records of products in a catalogue. 

We can query Solr using client SDK libraries, JDBC or simply using a HTTP API. Let's run a basic query using `curl`. 

`curl "http://localhost:8983/solr/techproducts/select?indent=on&q=*:*"`{{execute}}

This query uses a wildcard syntax (`*:*`) to fetch all documents in the index. 

Our results have the format: 

```
{
  "responseHeader":{
    "status":0,
    "QTime":1,
    "params":{
      "q":"*:*",
      "indent":"on"}},
  "response":{"numFound":32,"start":0,"docs":[
      {
        "id":"GB18030TEST",
        "name":["Test with some GB18030 encoded characters"],
        "features":["No accents here",
          "这是一个功能",
          "This is a feature (translated)",
          "这份文件是很有光泽",
          "This document is very shiny (translated)"],
        "price":[0.0],
        "inStock":[true],
        "_version_":1656331118163525632},
...
```

We can see that by default, this core returns results in `JSON` format, and that we found `32` results.

Good job! We now have a fully working Solr core which we can use to learn more about indexing and searching data.