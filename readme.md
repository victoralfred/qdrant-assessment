### GET the available shards on the cluster of 4 nodes

```bash
pip3 install -r requirements.txt
python3 app.py
```
```test
Type   | Shard Id | Shard Key  | State 
---------------------------------------
Remote | 1        | netherland | Active
Remote | 3        | netherland | Active
Remote | 4        | netherland | Active
Remote | 6        | germany    | Active
Remote | 7        | germany    | Active
Remote | 8        | germany    | Active
Remote | 9        | france     | Active
Remote | 10       | france     | Active
Remote | 11       | france     | Active
Local  | 2        | netherland | Active
Local  | 5        | germany    | Active
Local  | 12       | france     | Active
```