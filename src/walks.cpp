
#include "walks.hpp"
#include "embedding.hpp"
#include "gapprox_embed.hpp"
#include "trash_keeper.hpp"
#include "pattern.hpp"

namespace rwalk {
    void random_walk(Store& st);
    void initialize_walk(Store& st, Embedding& embeds, pattern& pat) {
        types::label_t lab;
        types::vlist_t vlist;
        st.get_random_l1(lab, vlist);
        INFO(*logger, lab << " and vlist size is" << vlist);
        /*
         * Create level 1 embeddings depending on the type of the algorithm that
         * we are running; gapprox_embedding to test GAPPROX method
         */
        if(true) {
            GApprox::GApproxEmbedding gap_embed;
            embeds = gap_embed;
            embeds.init_embeddings(lab, vlist);
        }
    }
    void walks(Store& st) {
        int numwalks = st.get_num_walks();
        for(int walk=0; walk < numwalks; walk) {
            random_walk(st);
        }
    }
    void random_walk(Store& st) {
        pattern pat;
        Embedding embeds;
        Janitor jtr;
        int toss;
        bool result;
        while(true) {
        } // end while
    }

    bool fwd_extension(Janitor& jtr,pattern& pat,Embedding& embeds, Store& st) {
        /* Shuffle the list of vertices from which the extension is tried and
         * the labels with which the extensions are tried from a given vertex
         * in the pattern
         */
        types::pat_vlist_t vertices;
        vector<types::label_t> labels;
        pat.get_vertices(vertices);
        st.get_labels(labels);
        st.myran.myshuffle(vertices);
        st.myran.myshuffle(labels);
        // Iterate over the complete set of possible extensions
        tr(vertices,it) {
            if(jtr.is_expired(*it))
                continue;
            tr(labels,it2) {
                if(jtr.is_failed_label(*it,*it2))
                    continue;
                else {
                    Embedding extend_embed = embeds.extend_fwd(st, *it2);
                    int sup = extend_embed.compute_support();
                    if(!sup) {
                        jtr.add_failed_label(*it,*it2);
                    }
                    else {
                        return true;
                    }
                }
            }
            jtr.add_expired_vertex(*it);
        }
        return false;
    }

    bool back_extension(Janitor& jtr,pattern& pat,Embedding& embeds, Store& st) {
        types::pat_e
        tr(vp,it) {
            if(jtr.is_back_fail(it->first,it->second))
                continue;
            else {
                int sup = 0; //TODO
                if(!sup) {
                }
                else {
                    return true;
                }
            }
        }
        return 0;
    }
}
