# PI-X-First


This is our proposal for the PI-X-First algorithm which is an extension of the PI-First algorithm.

PI denotes the round in which the heuristic is stopping to do exploring and switches to the exploitation phase. X represents the number of Worker Agents (WA) to use when this switch is effective.

The Article for the data can be found here: https://www.nature.com/articles/sdata2016127
The data can be downloaded from here: https://www.synapse.org/#!Synapse:syn5909526


## Development Requirements

- python 2.7
- sqlite 3
- pandas
- git
- The data from the experiement has to be copied to the subfolder /source_datafiles

## Executing Reuirements

- pandas
- The data from the experiement has to be copied to the subfolder /source_datafiles

## Execution
Please invoke this command with "python2 pi-x-first.py <pi> <nAgents> <numRounds> <alternativeReputation>"

"<alternativeReputation>" is an optional boolean parameter. If set to True, an alternative reputation model is used.
