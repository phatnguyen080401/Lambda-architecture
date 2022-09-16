CREATE TABLE IF NOT EXISTS twitter.twitter_lake (
    tweet_id double,
    created_at text,
    author text,
    retweet_count int,
    retweeted boolean,
    tweet_text text,
    user_description text,
    user_favourites double,
    user_followers double,
    user_friends double,
    user_id double,
    user_location text,
    user_name text,
    hashtags list<text>,
    PRIMARY KEY (tweet_id, created_at)
) WITH ID = 333f5630-304c-11ed-941c-2321bb7c1cad
    AND CLUSTERING ORDER BY (created_at ASC)
    AND additional_write_policy = '99p'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND cdc = false
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '16', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND extensions = {}
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99p';
