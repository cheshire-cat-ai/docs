# Overview

Lo stregatto è un micro framework di AI pronto all'uso, una volta installato ed eseguita la configurazione iniziale per il collegamento ad un LLM, può essere interrogato tramite delle API. Le API restituiscono la risposta data da l'LLM.  

Ma questo è solo l'inizio.

Le conversazioni intercorse vengono salvate in un database locale chiamato `episodic memory`, quando viene fatta una domanda la risposta viene data considerando anche le passate conversazioni.

Si possono caricare documenti testuali, anche questi documenti vengono salvati in un database locale chiamato `declarative memory`, le risposte verranno date considerando anche le informazioni presenti in questo documenti.
I documenti possono venire caricati sia tramite API ma anche tramite GUI.

Il componente che si occupa dell'ingestion dei documenti è il `Rabbit Hole`.

Ma lo stregatto non è in grado solo di rispondere a domande, può anche eseguire azioni, è possibile scrivere funzioni Python chiamate `tools` e fare in modo che l'LLM esegua questo codice, cosa il codice Python può fare è limitato solo dalla fantasia.

E' inoltre possibile adattare il core dello stregatto, nei principali flussi di processo sono definiti dei punti di adattamento chiamati `hooks`, è possibile scrivere function Python agganciabili a questi `hook`, il codice agganciato verrà richiamato durante l'esecuzione del flusso e potrà modificare il funzionamento interno dello stregatto, tutto questo senza dover modificare direttamente il core lo stregatto.

`Tools` e `Hooks` vengono pacchettizzati in `plugin` che possono essere installati posizionando i file in una determinata cartella o tramite GUI.
Il componente che si occupa di gestire i plugin è il Mad Hatter.

Completano il framework il portale web utilizzabile da utenti Admin, tramite questo portale è possibile configurare le impostazioni del framework, installare plugin, caricare documenti, ed è anche possibile utilizzarlo come strumento di playground, è possibile chattare con lo stregatto ed interrogare le memorie.