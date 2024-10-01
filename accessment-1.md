```
qdrant_node4  | 2024-10-01T15:48:59.353409Z ERROR qdrant::startup: Panic backtrace:
qdrant_node4  |    0: qdrant::startup::setup_panic_hook::{{closure}}
qdrant_node4  |    1: std::panicking::rust_panic_with_hook
qdrant_node4  |    2: std::panicking::begin_panic_handler::{{closure}}
qdrant_node4  |    3: std::sys::backtrace::__rust_end_short_backtrace
qdrant_node4  |    4: rust_begin_unwind
qdrant_node4  |    5: core::panicking::panic_fmt
qdrant_node4  |    6: core::result::unwrap_failed
qdrant_node4  |    7: core::result::Result<T,E>::expect
qdrant_node4  |    8: qdrant::main
qdrant_node4  |    9: std::sys::backtrace::__rust_begin_short_backtrace
qdrant_node4  |   10: main
qdrant_node4  |   11: <unknown>
qdrant_node4  |   12: __libc_start_main
qdrant_node4  |   13: _start
qdrant_node4  |
qdrant_node4  | 2024-10-01T15:48:59.354067Z ERROR qdrant::startup: Panic occurred in file src/main.rs at line 330: Can't initialize consensus: Failed to initialize Consensus for new Raft state: Failed to create timeout channel: transport error
...
qdrant_node1  | 2024-10-01T15:49:02.814014Z  WARN storage::content_manager::consensus_manager: Failed to send message to http://qdrant_node3:6335/ with error: Error in closure supplied to transport channel pool: status: Unavailable, message: "Failed to connect to http://qdrant_node3:6335/, error: transport error", details: [], metadata: MetadataMap { headers: {} }
```